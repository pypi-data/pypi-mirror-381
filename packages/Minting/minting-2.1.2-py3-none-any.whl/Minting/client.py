
import requests
import pandas as pd
import io
import time
import os
import sys
from datetime import datetime
from pymongo import MongoClient


# ----------------- Database Layer -----------------
class Database:
    def __init__(self, mongo_uri, db_name):
        
        try:
            self.client = MongoClient(
                mongo_uri,
                serverSelectionTimeoutMS=5000,
                connectTimeoutMS=10000
            )
            # Test connection
            self.client.server_info()
            self.db = self.client[db_name]
            
        except Exception as e:
            print(f"❌ Connection Error: {e}")
            raise

        self.users = self.db["users"]
        self.access_tokens = self.db["accesstokens"]
        self.user_plans = self.db["userplans"]
        self.plans = self.db["plans"]


# ----------------- Token Manager -----------------
class TokenManager:
    def __init__(self, db: Database, raw_token: str):
        self.db = db
        self.token = raw_token.strip()

    def check_token_and_credits(self):
        """Validate token and check if user has credits"""
        token_doc = self.db.access_tokens.find_one({
            "token": self.token,
            "isActive": True
        })
        
        if not token_doc:
            return {"valid": False, "error": "Invalid or inactive access token"}

        user_id = token_doc["userId"]

        plan_doc = self.db.user_plans.find_one({
            "userId": user_id,
            "isActive": True,
            "expiresAt": {"$gte": datetime.utcnow()}
        })

        if not plan_doc:
            return {"valid": False, "error": "No active subscription plan found"}

        credits = plan_doc.get("creditsRemaining", 0)

        # If credits <= 0, show warning but allow execution
        if credits <= 0:
            print("⚠️  Credits exhausted")

        return {
            "valid": True,   # Always allow execution
            "userId": user_id,
            "planId": plan_doc["_id"],
            "creditsRemaining": max(credits, 0)  # Never display negative
        }

    def deduct_credit(self):
        """Deduct one credit (can go negative internally, but display will cap at 0)"""
        token_doc = self.db.access_tokens.find_one({
            "token": self.token,
            "isActive": True
        })
        
        if not token_doc:
            return False

        user_id = token_doc["userId"]

        plan_doc = self.db.user_plans.find_one({
            "userId": user_id,
            "isActive": True,
            "expiresAt": {"$gte": datetime.utcnow()}
        })

        if not plan_doc:
            return False

        # Allow decrement even if credits are 0 (can go negative in DB)
        result = self.db.user_plans.update_one(
            {"_id": plan_doc["_id"]},
            {
                "$inc": {"creditsRemaining": -1},
                "$set": {"updatedAt": datetime.utcnow()}
            }
        )
        return result.modified_count > 0

    def get_remaining_credits(self):
        """Get remaining credits (never negative for display)"""
        token_doc = self.db.access_tokens.find_one({
            "token": self.token,
            "isActive": True
        })
        
        if not token_doc:
            return 0

        user_id = token_doc["userId"]

        plan_doc = self.db.user_plans.find_one({
            "userId": user_id,
            "isActive": True,
            "expiresAt": {"$gte": datetime.utcnow()}
        })

        if not plan_doc:
            return 0

        # Show 0 if negative
        return max(plan_doc.get("creditsRemaining", 0), 0)

# class TokenManager:
#     def __init__(self, db: Database, raw_token: str):
#         self.db = db
#         self.token = raw_token.strip()

#     def check_token_and_credits(self):
#         """Validate token and check if user has credits"""
#         token_doc = self.db.access_tokens.find_one({
#             "token": self.token,
#             "isActive": True
#         })
        
#         if not token_doc:
#             return {"valid": False, "error": "Invalid or inactive access token"}

#         user_id = token_doc["userId"]

#         plan_doc = self.db.user_plans.find_one({
#             "userId": user_id,
#             "isActive": True,
#             "expiresAt": {"$gte": datetime.utcnow()}
#         })

#         if not plan_doc:
#             return {"valid": False, "error": "No active subscription plan found"}

#         credits = plan_doc.get("creditsRemaining", 0)

#         if credits <= 0:
#             print(f"error: Credits Expired")

#         return {
#             "valid": True,
#             "userId": user_id,
#             "planId": plan_doc["_id"],
#             "creditsRemaining": credits
#         }

#     def deduct_credit(self):
#         """Deduct one credit from user's plan"""
#         token_doc = self.db.access_tokens.find_one({
#             "token": self.token,
#             "isActive": True
#         })
        
#         if not token_doc:
#             return False

#         user_id = token_doc["userId"]

#         plan_doc = self.db.user_plans.find_one({
#             "userId": user_id,
#             "isActive": True,
#             "expiresAt": {"$gte": datetime.utcnow()}
#         })

#         if not plan_doc:
#             return False

#         result = self.db.user_plans.update_one(
#             {"_id": plan_doc["_id"], "creditsRemaining": {"$gt": 0}},
#             {
#                 "$inc": {"creditsRemaining": -1},
#                 "$set": {"updatedAt": datetime.utcnow()}
#             }
#         )
        
#         return result.modified_count > 0

#     def get_remaining_credits(self):
#         """Get remaining credits for the token's user"""
#         token_doc = self.db.access_tokens.find_one({
#             "token": self.token,
#             "isActive": True
#         })
        
#         if not token_doc:
#             return 0

#         user_id = token_doc["userId"]

#         plan_doc = self.db.user_plans.find_one({
#             "userId": user_id,
#             "isActive": True,
#             "expiresAt": {"$gte": datetime.utcnow()}
#         })

#         return plan_doc.get("creditsRemaining", 0) if plan_doc else 0


# ----------------- Client Class -----------------
class Client:
    def __init__(
        self,
        access_token,
        base_url="http://34.172.210.29/predict",
        mongo_uri="mongodb+srv://ankitarrow:ankitarrow@cluster0.zcajdur.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
        db_name="test"
    ):
        self.base_url = base_url
        self.access_token = access_token.strip()
        
        print("="*60)
        print("🚀 Initializing Mintzy")
        print("="*60)

        self.db = Database(mongo_uri, db_name)
        self.token_manager = TokenManager(self.db, self.access_token)

    def _format_table(self, response_json, tickers, parameters):
        """Format API response into pandas DataFrame"""
        try:
            rows = []
            result = response_json.get("result", {})

            for ticker in tickers:
                for param in parameters:
                    if ticker not in result or param not in result[ticker]:
                        rows.append(pd.DataFrame([{
                            "Ticker": ticker,
                            "Parameter": param,
                            "Error": "No prediction data available"
                        }]))
                        continue

                    raw_data = result[ticker][param].get("data", "")
                    if not raw_data:
                        rows.append(pd.DataFrame([{
                            "Ticker": ticker,
                            "Parameter": param,
                            "Error": "Empty prediction data"
                        }]))
                        continue

                    df = pd.read_csv(io.StringIO(raw_data), sep=r"\s+", engine="python")
                    df["Date"] = pd.to_datetime(df["Timestamp"]).dt.date
                    df["Time"] = pd.to_datetime(df["Timestamp"]).dt.time
                    
                    pred_col = f"Predicted_{param.capitalize()}"
                    if pred_col in df.columns:
                        df.rename(columns={pred_col: "Predicted Price"}, inplace=True)
                    
                    df["Ticker"] = ticker
                    rows.append(df[["Ticker", "Date", "Time", "Predicted Price"]])

            if rows:
                return pd.concat(rows, ignore_index=True)
            else:
                return pd.DataFrame([{"Error": "No data to display"}])
                
        except Exception as e:
            return pd.DataFrame([{"Error": str(e)}])

    def get_prediction(self, tickers, time_frame, parameters):
        """
        Get stock predictions (single run only, no auto-refresh).
        
        Args:
            tickers: String or list of stock tickers (max 3)
            time_frame: Time frame for predictions (e.g., "4 hours", "1 day")
            parameters: String or list of parameters to predict (e.g., ["close", "open"])
        
        Returns:
            dict: Response with success status and data/error
        """
        # Normalize tickers
        if isinstance(tickers, str):
            tickers = [tickers]
        if not isinstance(tickers, list):
            return {"success": False, "error": "Tickers must be a string or list"}
        if len(tickers) > 3:
            return {"success": False, "error": "Maximum of 3 tickers allowed"}

        # Normalize parameters
        if isinstance(parameters, str):
            parameters = [parameters]

        try:
            print("\n" + "="*60)
            print("📊 Getting Predictions")
            print("="*60)
            
            # Check token and credits
            token_check = self.token_manager.check_token_and_credits()
            if not token_check["valid"]:
                print(f"❌ {token_check['error']}")
                return {"success": False, "error": token_check["error"]}

            print(f"Tickers: {', '.join(tickers)}")
            print(f" Time Frame: {time_frame}")
            print(f"Parameters: {', '.join(parameters)}")

            # Prepare payload
            payload = {
                "action": {
                    "action_type": "predict",
                    "predict": {
                        "given": {
                            "ticker": tickers,
                            "time_frame": time_frame
                        },
                        "required": {
                            "parameters": parameters
                        }
                    }
                }
            }

            # Send request
            print("\n⏳ Fetching Predictions ...")
            response = requests.post(
                self.base_url,
                json=payload,
                headers={"X-Access-Token": self.access_token},
                timeout=30
            )
            response.raise_for_status()
            response_json = response.json()
            
            

            # Format results
            df = self._format_table(response_json, tickers, parameters)

            # Deduct credit
            if self.token_manager.deduct_credit():
                remaining = self.token_manager.get_remaining_credits()
            else:
                remaining = token_check["creditsRemaining"] - 1

            # Display results
            print("\n" + "="*60)
            print(f"📊 Predictions ({time_frame})")
            print("="*60)
            print(df.to_string(index=False))
            print("="*60)
            print(f"💳 Remaining credits: {remaining}")
            print("="*60)

            return {
                "success": True,
                "data": df,
                "credits_remaining": remaining,
                "timestamp": datetime.now().isoformat()
            }

        except requests.exceptions.Timeout:
            error_msg = "Request timed out. Please try again."
            print(f"❌ {error_msg}")
            return {"success": False, "error": error_msg}

        except requests.exceptions.RequestException as e:
            error_msg = f"API request failed: {str(e)}"
            print(f"❌ {error_msg}")
            return {"success": False, "error": error_msg}

        except Exception as e:
            error_msg = f"Unexpected error: {str(e)}"
            print(f"❌ {error_msg}")
            return {"success": False, "error": error_msg}

    def get_credits(self):
        """Get remaining credits for the current token"""
        credits = self.token_manager.get_remaining_credits()
        print(f"💳 Remaining credits: {credits}")
        return credits
