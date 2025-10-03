# BSE Option Chain Scraper

This repository provides an **Unofficial Python API** to fetch **Option Chain Data** from the [BSE India](https://www.bseindia.com) website.

The scraper uses `requests` and `mthrottle` with proper headers and endpoints exposed by BSE’s API to return option chain data in a structured JSON format, similar to NSE’s option chain format.

---

## 🚀 Features
- Fetch **all available expiries** for Sensex (or other symbols by `scrip_cd`).
- Fetch option chain data for a **single expiry**.
- Fetch and merge option chain data for **all expiries at once**.
- Data is formatted with **CE (Call)** and **PE (Put)** separated, making it analysis-friendly.
- Optionally save the output to `.json` files for further processing.

---

## 📦 Installation

Clone the repo and install dependencies with uv:

```bash
git clone <reponame>
uv sync 