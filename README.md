# Online Polling and Voting System

## Overview
Python program jo lists ki help se votes record karta hai, duplicate voting rokta hai aur results percentage ke saath dikhata hai.

## Installation / How to Run
1. Python 3 install karo

2. git clone https://github.com/akanshriborkar205-art/polling-voting-system.git

3. python voting_system.py

## Logic Summary
- candidates[] mein naam, votes[] mein counts (same index)
- voted_users mein use ho chuki IDs; wahi ID dobara aaye to vote reject
- percentage = votes / total_votes * 100
