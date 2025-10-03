from __future__ import annotations

import json
from mthrottle import Throttle
from requests import Session

throttle_config = {
    "lookup": {
        "rps": 15,
    },
    "default": {
        "rps": 8,
    },
}

th = Throttle(throttle_config, 15)


class BSEOption:
    """
    Unofficial Python Api for BSE India for fetching option chain data
    """

    version = "3.1.0"
    origin_url = "https://www.bseindia.com"
    referer_url = "https://www.bseindia.com/"
    api_url = "https://api.bseindia.com/BseIndiaAPI/api"

    __optionIndex = ("sensex")
    
    # init function for header and session handling 
    def __init__(self):
        self.session = Session()
        origin_url = "https://www.bseindia.com"
        referer_url = "https://www.bseindia.com/"
        self.session.headers.update(
            {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0",
                "Accept": "application/json, text/plain, */*",
                "Accept-Language": "en-US,en;q=0.9",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Origin": origin_url,
                "Referer": referer_url,
                "Sec-Fetch-Site": "same-site",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Dest": "empty",
                "Sec-CH-Ua": '"Not)A;Brand";v="8", "Chromium";v="138", "Microsoft Edge";v="138"',
                "Sec-Ch-Ua-Mobile": "?0",
                "Sec-Ch-Ua-Platform": '"Windows"',
            }
        )

    # Function to get the list of all the available expiries from BSE website     
    def get_expiries(self, scrip_cd="1"):
        """Fetch expiry dates directly from expiry API"""
        url = f"{self.api_url}/ddlExpiry_IV/w"
        params = {"ProductType": "IO", "scrip_cd": scrip_cd}
        resp = self.session.get(url, params=params)
        resp.raise_for_status()
        data = resp.json()
        expiries = [row["ExpiryDate"] for row in data.get("Table1", [])]
        return expiries
    
    # Function to get the data of option chain from the BSE website
    def get_option_chain(self, expiry: str, scrip_cd="1", json_save: bool = False):
        """Fetch, format and optionally save option chain data for a given expiry"""
        expiry_fmt = expiry.replace(" ", "+")
        url = f"{self.api_url}/DerivOptionChain_IV/w?Expiry={expiry_fmt}&scrip_cd={scrip_cd}&strprice=0"
        resp = self.session.get(url)
        resp.raise_for_status()
        data = resp.json()

        table = data.get("Table", [])
        if not table:
            print(f"⚠️ Empty table for {expiry}")
            result = {"records": {"expiryDates": [expiry], "data": []}}
        else:
            print(f"✅ Got {len(table)} rows for {expiry}")
            formatted = []
            for row in table:
                record = {
                    "strikePrice": float(row["Strike_Price1"]),
                    "expiryDate": expiry,
                    "CE": {
                        "Series_Code": row.get("C_Series_Code"),
                        "Open_Interest": row.get("C_Open_Interest"),
                        "Change_in_OI": row.get("C_Absolute_Change_OI"),
                        "LastPrice": row.get("C_Last_Trd_Price"),
                        "Change": row.get("C_NetChange"),
                        "Volume": row.get("C_Vol_Traded"),
                        "BidQty": row.get("C_BIdQty"),
                        "BidPrice": row.get("C_BidPrice"),
                        "AskPrice": row.get("C_OfferPrice"),
                        "AskQty": row.get("C_OfferQty"),
                        "Series_Id": row.get("C_Series_Id"),
                        "SCRIP_ID": row.get("C_SCRIP_ID"),
                        "CompanyName": row.get("C_comapny_name"),
                        "IV": row.get("C_IV"),
                        "underlyingValue": row.get("UlaValue")
                    },
                    "PE": {
                        "Series_Code": row.get("p_Series_Code"),
                        "Open_Interest": row.get("Open_Interest"),
                        "Change_in_OI": row.get("Absolute_Change_OI"),
                        "LastPrice": row.get("Last_Trd_Price"),
                        "Change": row.get("NetChange"),
                        "Volume": row.get("Vol_Traded"),
                        "BidQty": row.get("BIdQty"),
                        "BidPrice": row.get("BidPrice"),
                        "AskPrice": row.get("OfferPrice"),
                        "AskQty": row.get("OfferQty"),
                        "Series_Id": row.get("Series_Id"),
                        "SCRIP_ID": row.get("SCRIP_ID"),
                        "CompanyName": row.get("comapny_name"),
                        "IV": row.get("IV"),
                        "underlyingValue": row.get("UlaValue")
                    }
                }
                formatted.append(record)

            result = {"records": {"expiryDates": [expiry], "data": formatted}}

        # Optionally save JSON file
        if json_save:
            fname = f"{expiry.replace(' ', '_')}_bse_option.json"
            with open(fname, "w", encoding="utf-8") as f:
                json.dump(result, f, indent=2)
            print(f"💾 Saved option chain data to {fname}")

        return result

    # Function to get the data of all expiries option chains.    
    def get_all_option_chains(self, scrip_cd="1"):
        """Fetch option chain data for ALL expiries"""
        json_save=False
        expiries = self.get_expiries(scrip_cd)
        print("Expiries found:", expiries)

        all_data = {"records": {"expiryDates": expiries, "data": []}}
        for expiry in expiries:
            print(f"Fetching option chain for {expiry}...")
            result = self.get_option_chain(expiry, scrip_cd, json_save)
            all_data["records"]["data"].extend(result["records"]["data"])

        fname = f"bse_option_chain_all_expiry.json"
        with open(fname, "w", encoding="utf-8") as f:
            json.dump(all_data, f, indent=2)
        print(f"💾 Saved option chain data for all expiries to {fname}")
    
    
   