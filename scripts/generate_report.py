import requests
import csv
from datetime import datetime

def export_campaign_results(campaign_id: str, saviynt_url: str, token: str) -> list:
    """
    Export access certification results from a Saviynt campaign.
    """
    response = requests.get(
        f"{saviynt_url}/ECM/api/v5/campaign/getCampaignUserDetails",
        headers={"Authorization": f"Bearer {token}"},
        params={"campaignId": campaign_id, "max": 1000, "offset": 0}
    )
    response.raise_for_status()
    return response.json().get("certificationDetails", [])

def write_csv(results: list, outfile: str):
    if not results:
        print("No results to write.")
        return
    with open(outfile, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=results[0].keys())
        writer.writeheader()
        writer.writerows(results)
    print(f"Exported {len(results)} records to {outfile}")
