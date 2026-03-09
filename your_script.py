import pandas as pd

# Load CSV files
user_referrals = pd.read_csv("data/user_referrals.csv")
user_referral_logs = pd.read_csv("data/user_referral_logs.csv")
user_logs = pd.read_csv("data/user_logs.csv")
referral_rewards = pd.read_csv("data/referral_rewards.csv")
paid_transactions = pd.read_csv("data/paid_transactions.csv")

# Merge some useful tables
df = user_referrals.merge(
    user_referral_logs,
    left_on="referral_id",
    right_on="user_referral_id",
    how="left"
)

df = df.merge(
    referral_rewards,
    left_on="referral_reward_id",
    right_on="id",
    how="left"
)

# Fill missing reward values
if "reward_value" in df.columns:
    df["reward_value"] = pd.to_numeric(df["reward_value"], errors="coerce").fillna(0)

# Simple validation column
df["is_business_logic_valid"] = df["reward_value"] > 0

# Save report
df.to_csv("referral_report.csv", index=False)

print("Report Generated Successfully")