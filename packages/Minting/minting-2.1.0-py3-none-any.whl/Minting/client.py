# import requests
# import pandas as pd
# import time
# import io
# from datetime import datetime
# from pymongo import MongoClient

# class Client:
#     def __init__(self, access_token, base_url="http://34.172.210.29/predict", mongo_uri="mongodb+srv://ankitarrow:ankitarrow@cluster0.zcajdur.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0", db_name="ankitarrow"):
#         self.base_url = base_url
#         self.access_token = access_token
#         self.mongo_uri = mongo_uri
#         self.db_name = db_name
#         # Connect to MongoDB Atlas
#         print("Connecting to MongoDB Atlas...")
#         self.client = MongoClient(self.mongo_uri)
#         self.db = self.client[self.db_name]
#         self.users = self.db["user"]  # equivalent to users collection
#         print("Connected to MongoDB:", self.db_name)

#     def _check_token(self):    ## change this 
#         """Check token in MongoDB and verify credits"""
#         user = self.users.find_one({"access_token": self.access_token})
#         if not user:
#             return {"valid": False, "error": "Invalid access token"}
#         if user.get("credits", 0) <= 0:
#             return {"valid": False, "error": "Insufficient credits contact support : mintzy01.ai@gmail.com"}
#         return {"valid": True, "user": user}

#     def _deduct_credit(self):   ## chnge this 
#         """Deduct 1 credit in MongoDB"""
#         self.users.update_one(
#             {"access_token": self.access_token},
#             {"$inc": {"credits": -1}}
#         )

#     def _get_remaining_credits(self):    ## change this 
#         """Fetch remaining credits"""
#         user = self.users.find_one({"access_token": self.access_token})
#         return user.get("credits", 0) if user else 0

#     def _format_table(self, response_json, tickers, parameters):
#         try:
#             rows = []
#             result = response_json.get("result", {})  

#             for ticker in tickers:
#                 for param in parameters:
#                     if ticker not in result or param not in result[ticker]:
#                         rows.append(pd.DataFrame([{
#                             "Ticker": ticker,
#                             "Parameter": param,
#                             "Error": "No prediction data available"
#                         }]))
#                         continue

#                     raw_data = result[ticker][param].get("data", "")
#                     if not raw_data:
#                         rows.append(pd.DataFrame([{
#                             "Ticker": ticker,
#                             "Parameter": param,
#                             "Error": "Empty prediction data"
#                         }]))
#                         continue

#                     df = pd.read_csv(io.StringIO(raw_data), sep=r"\s+", engine="python")
#                     df["Date"] = pd.to_datetime(df["Timestamp"]).dt.date
#                     df["Time"] = pd.to_datetime(df["Timestamp"]).dt.time
#                     df.rename(columns={f"Predicted_{param.capitalize()}": "Predicted Price"}, inplace=True)
#                     df["Ticker"] = ticker
#                     rows.append(df[["Ticker", "Date", "Time", "Predicted Price"]])

#             final_df = pd.concat(rows, ignore_index=True)
#             return final_df
#         except Exception as e:
#             return pd.DataFrame([{"Error": str(e)}])

#     def get_prediction(self, tickers, time_frame, parameters):
#         # Check token validity in DB
#         token_check = self._check_token()
#         if not token_check["valid"]:
#             return {"success": False, "error": token_check["error"]}

#         if isinstance(tickers, str):
#             tickers = [tickers]
#         if not isinstance(tickers, list):
#             return {"success": False, "error": "Tickers must be a string or list"}
#         if len(tickers) > 3:
#             return {"success": False, "error": "Maximum of 3 tickers allowed"}

#         if isinstance(parameters, str):
#             parameters = [parameters]

#         payload = {
#             "action": {
#                 "action_type": "predict",
#                 "predict": {
#                     "given": {"ticker": tickers, "time_frame": time_frame},
#                     "required": {"parameters": parameters}
#                 }
#             }
#         }

#         while True:
#             try:
#                 response = requests.post(
#                     self.base_url,
#                     json=payload,
#                     headers={"X-Access-Token": self.access_token},
#                     timeout=30
#                 )
#                 response.raise_for_status()
#                 response_json = response.json()

#                 df = self._format_table(response_json, tickers, parameters)

#                 # Deduct credit in DB
#                 self._deduct_credit()

#                 # Show predictions
#                 print("\033c", end="")
#                 print(f"Live Predictions ({time_frame}) — {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
#                 print(df.to_string(index=False))
#                 print(f"Remaining credits: {self._get_remaining_credits()}")

#             except requests.exceptions.RequestException as e:
#                 print(f"⚠️ Error: {e}")

#             time.sleep(900)  # 15 minutes refresh




# import requests
# import pandas as pd
# import time
# import io
# from datetime import datetime
# from pymongo import MongoClient


# # ----------------- Database Layer -----------------
# class Database:
#     def __init__(self, mongo_uri, db_name):
#         print("Connecting to MongoDB Atlas...")
#         self.client = MongoClient(mongo_uri)
#         self.db = self.client[db_name]
#         print("Connected to MongoDB:", db_name)

#         # Collections
#         self.users = self.db["users"]
#         self.access_tokens = self.db["accesstokens"]
#         self.user_plans = self.db["userplans"]
#         self.plans = self.db["plans"]


# # ----------------- Token Manager -----------------
# class TokenManager:
#     def __init__(self, db: Database, token: str):
#         self.db = db
#         self.token = token

#     def check_token_and_credits(self):
#         token_doc = self.db.access_tokens.find_one({"token": self.token, "isActive": True})
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

#         if plan_doc.get("creditsRemaining", 0) <= 0:
#             return {"valid": False, "error": "Insufficient credits, please upgrade or renew plan"}

#         return {
#             "valid": True,
#             "userId": user_id,
#             "planId": plan_doc["_id"],
#             "creditsRemaining": plan_doc["creditsRemaining"]
#         }

#     def deduct_credit(self):
#         token_doc = self.db.access_tokens.find_one({"token": self.token, "isActive": True})
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
#         token_doc = self.db.access_tokens.find_one({"token": self.token, "isActive": True})
#         if not token_doc:
#             return 0

#         user_id = token_doc["userId"]

#         plan_doc = self.db.user_plans.find_one({
#             "userId": user_id,
#             "isActive": True,
#             "expiresAt": {"$gte": datetime.utcnow()}
#         })

#         return plan_doc.get("creditsRemaining", 0) if plan_doc else 0


# # ----------------- Client Class -----------------
# class Client:
#     def __init__(self, access_token, base_url="http://34.172.210.29/predict",
#                  mongo_uri="mongodb+srv://ankitarrow:ankitarrow@cluster0.zcajdur.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
#                  db_name="ankitarrow"):
#         self.base_url = base_url
#         self.access_token = access_token

#         # Init DB + Token Manager
#         self.db = Database(mongo_uri, db_name)
#         self.token_manager = TokenManager(self.db, self.access_token)

#     def _format_table(self, response_json, tickers, parameters):
#         try:
#             rows = []
#             result = response_json.get("result", {})

#             for ticker in tickers:
#                 for param in parameters:
#                     if ticker not in result or param not in result[ticker]:
#                         rows.append(pd.DataFrame([{
#                             "Ticker": ticker,
#                             "Parameter": param,
#                             "Error": "No prediction data available"
#                         }]))
#                         continue

#                     raw_data = result[ticker][param].get("data", "")
#                     if not raw_data:
#                         rows.append(pd.DataFrame([{
#                             "Ticker": ticker,
#                             "Parameter": param,
#                             "Error": "Empty prediction data"
#                         }]))
#                         continue

#                     df = pd.read_csv(io.StringIO(raw_data), sep=r"\s+", engine="python")
#                     df["Date"] = pd.to_datetime(df["Timestamp"]).dt.date
#                     df["Time"] = pd.to_datetime(df["Timestamp"]).dt.time
#                     df.rename(columns={f"Predicted_{param.capitalize()}": "Predicted Price"}, inplace=True)
#                     df["Ticker"] = ticker
#                     rows.append(df[["Ticker", "Date", "Time", "Predicted Price"]])

#             return pd.concat(rows, ignore_index=True)
#         except Exception as e:
#             return pd.DataFrame([{"Error": str(e)}])
        
#     def get_prediction(self, tickers, time_frame, parameters):
#         token_check = self.token_manager.check_token_and_credits()
#         print("Token check result:", token_check)   # DEBUG LINE
#         if not token_check["valid"]:
#             return {"success": False, "error": token_check["error"]}

#         if isinstance(tickers, str):
#             tickers = [tickers]
#         if not isinstance(tickers, list):
#             return {"success": False, "error": "Tickers must be a string or list"}
#         if len(tickers) > 3:
#             return {"success": False, "error": "Maximum of 3 tickers allowed"}

#         if isinstance(parameters, str):
#             parameters = [parameters]

#         payload = {
#             "action": {
#                 "action_type": "predict",
#                 "predict": {
#                     "given": {"ticker": tickers, "time_frame": time_frame},
#                     "required": {"parameters": parameters}
#                 }
#             }
#         }

#         try:
#             response = requests.post(
#                 self.base_url,
#                 json=payload,
#                 headers={"X-Access-Token": self.access_token},
#                 timeout=30
#             )
#             response.raise_for_status()
#             response_json = response.json()
#             print("Raw Response:", response_json)  # 🔎 DEBUG LINE

#             df = self._format_table(response_json, tickers, parameters)

#             # Deduct credit
#             self.token_manager.deduct_credit()

#             # Display predictions
#             print("\033c", end="")
#             print(f"Live Predictions ({time_frame}) — {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
#             print(df.to_string(index=False))
#             print(f"Remaining credits: {self.token_manager.get_remaining_credits()}")

#         except requests.exceptions.RequestException as e:
#             print(f"⚠️ Error: {e}")


#     # def get_prediction(self, tickers, time_frame, parameters):
#     #     token_check = self.token_manager.check_token_and_credits()
#     #     if not token_check["valid"]:
#     #         return {"success": False, "error": token_check["error"]}

#     #     if isinstance(tickers, str):
#     #         tickers = [tickers]
#     #     if not isinstance(tickers, list):
#     #         return {"success": False, "error": "Tickers must be a string or list"}
#     #     if len(tickers) > 3:
#     #         return {"success": False, "error": "Maximum of 3 tickers allowed"}

#     #     if isinstance(parameters, str):
#     #         parameters = [parameters]

#     #     payload = {
#     #         "action": {
#     #             "action_type": "predict",
#     #             "predict": {
#     #                 "given": {"ticker": tickers, "time_frame": time_frame},
#     #                 "required": {"parameters": parameters}
#     #             }
#     #         }
#     #     }

#     #     while True:
#     #         try:
#     #             response = requests.post(
#     #                 self.base_url,
#     #                 json=payload,
#     #                 headers={"X-Access-Token": self.access_token},
#     #                 timeout=30
#     #             )
#     #             response.raise_for_status()
#     #             response_json = response.json()

#     #             df = self._format_table(response_json, tickers, parameters)

#     #             # Deduct credit
#     #             self.token_manager.deduct_credit()

#     #             # Display predictions
#     #             print("\033c", end="")
#     #             print(f"Live Predictions ({time_frame}) — {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
#     #             print(df.to_string(index=False))
#     #             print(f"Remaining credits: {self.token_manager.get_remaining_credits()}")

#     #         except requests.exceptions.RequestException as e:
#     #             print(f"⚠️ Error: {e}")

#             time.sleep(900)  # Refresh every 15 mins


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
        print("Connecting to MongoDB Atlas...")
        try:
            self.client = MongoClient(
                mongo_uri,
                serverSelectionTimeoutMS=5000,
                connectTimeoutMS=10000
            )
            # Test connection
            self.client.server_info()
            self.db = self.client[db_name]
            print(f"✅ Connected to MongoDB: {db_name}")
        except Exception as e:
            print(f"❌ MongoDB Connection Error: {e}")
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

        if credits <= 0:
            return {"valid": False, "error": "Insufficient credits, please upgrade or renew plan"}

        return {
            "valid": True,
            "userId": user_id,
            "planId": plan_doc["_id"],
            "creditsRemaining": credits
        }

    def deduct_credit(self):
        """Deduct one credit from user's plan"""
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

        result = self.db.user_plans.update_one(
            {"_id": plan_doc["_id"], "creditsRemaining": {"$gt": 0}},
            {
                "$inc": {"creditsRemaining": -1},
                "$set": {"updatedAt": datetime.utcnow()}
            }
        )
        
        return result.modified_count > 0

    def get_remaining_credits(self):
        """Get remaining credits for the token's user"""
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

        return plan_doc.get("creditsRemaining", 0) if plan_doc else 0


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
        print("🚀 Initializing Minting Client")
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

    def get_prediction(self, tickers, time_frame, parameters, auto_refresh=True, refresh_interval=900):
        """
        Get stock predictions with auto-refresh (default: enabled)
        
        Args:
            tickers: String or list of stock tickers (max 3)
            time_frame: Time frame for predictions (e.g., "4 hours", "1 day")
            parameters: String or list of parameters to predict (e.g., ["close", "open"])
            auto_refresh: If True, continuously refresh predictions (default: True)
            refresh_interval: Seconds between refreshes (default: 900 = 15 minutes)
        
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
            iteration = 1
            while True:
                # Clear screen for refresh
                if auto_refresh and iteration > 1:
                    os.system('cls' if os.name == 'nt' else 'clear')
                
                print("\n" + "="*60)
                print("📊 Getting Predictions")
                print("="*60)
                
                # Check token and credits
                token_check = self.token_manager.check_token_and_credits()
                
                if not token_check["valid"]:
                    print(f"❌ {token_check['error']}")
                    return {"success": False, "error": token_check["error"]}

                print(f"📈 Tickers: {', '.join(tickers)}")
                print(f"⏱️  Time Frame: {time_frame}")
                print(f"📋 Parameters: {', '.join(parameters)}")

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

                try:
                    print("\n⏳ Sending request to prediction API...")
                    response = requests.post(
                        self.base_url,
                        json=payload,
                        headers={"X-Access-Token": self.access_token},
                        timeout=30
                    )
                    response.raise_for_status()
                    response_json = response.json()
                    
                    print("✅ Received response from API")

                    # Format results
                    df = self._format_table(response_json, tickers, parameters)

                    # Deduct credit
                    if self.token_manager.deduct_credit():
                        remaining = self.token_manager.get_remaining_credits()
                    else:
                        remaining = token_check["creditsRemaining"] - 1

                    # Display results
                    print("\n" + "="*60)
                    print(f"📊 Live Predictions ({time_frame})")
                    print(f"🕒 Generated at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
                    print("="*60)
                    print(df.to_string(index=False))
                    print("="*60)
                    print(f"💳 Remaining credits: {remaining}")
                    print("="*60)

                    # If not auto-refresh, return after first iteration
                    if not auto_refresh:
                        return {
                            "success": True,
                            "data": df,
                            "credits_remaining": remaining,
                            "timestamp": datetime.now().isoformat()
                        }

                    # Wait for next refresh (no countdown display)
                    print(f"\n⏰ Next update at {(datetime.now().timestamp() + refresh_interval).__format__('')}")
                    next_update_time = datetime.fromtimestamp(datetime.now().timestamp() + refresh_interval)
                    print(f"⏰ Next update at {next_update_time.strftime('%Y-%m-%d %H:%M:%S')} (Press Ctrl+C to stop)\n")
                    time.sleep(refresh_interval)
                    
                    iteration += 1

                except requests.exceptions.Timeout:
                    error_msg = "Request timed out. Please try again."
                    print(f"❌ {error_msg}")
                    if not auto_refresh:
                        return {"success": False, "error": error_msg}
                    print("⏳ Retrying in 30 seconds...")
                    time.sleep(30)
                    
                except requests.exceptions.RequestException as e:
                    error_msg = f"API request failed: {str(e)}"
                    print(f"❌ {error_msg}")
                    if not auto_refresh:
                        return {"success": False, "error": error_msg}
                    print("⏳ Retrying in 30 seconds...")
                    time.sleep(30)

        except KeyboardInterrupt:
            print("\n\n⏹️  Auto-refresh stopped by user")
            return {"success": True, "message": "Stopped by user"}
            
        except Exception as e:
            error_msg = f"Unexpected error: {str(e)}"
            print(f"❌ {error_msg}")
            return {"success": False, "error": error_msg}

    def get_credits(self):
        """Get remaining credits for the current token"""
        credits = self.token_manager.get_remaining_credits()
        print(f"💳 Remaining credits: {credits}")
        return credits
