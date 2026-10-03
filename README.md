# 🎓 UniFind — Terminal-Based Campus Lost & Found System

UniFind is a lightweight, terminal-based Python application designed to help university students report, track, and manage lost and found items on campus. By leveraging structured JSON storage and an intelligent fuzzy-matching algorithm, UniFind makes reconnecting lost items with their owners quick and reliable without requiring complex database setups.

---

## ✨ Features

* **Item Registration:** Easily report lost or found items with detailed metadata (category, color, location, date, and description).
* **Smart Matching System:** Automatically matches lost items with reported found items using a 4-point scoring model based on item details.
* **Flexible Search:** Search items by name (case-insensitive), category, location, or report type.
* **Item Management:** Claim found items or remove outdated reports with built-in confirmation safeguards.
* **Persistent Data:** Stores all reports in `lost_found.json` so data persists across application runs.
* **Robust Input Validation:** Enforces non-empty input, predefined campus locations/categories, and valid non-future date formats (`YYYY-MM-DD`).

---

## 🛠️ Architecture & Tech Stack

* **Language:** Python 3.x
* **Dependencies:** Python Standard Library (no external packages required)
* **Storage:** `lost_found.json`
* **Testing:** `pytest`

### 🔍 How the Matching Algorithm Works

UniFind uses a custom point-based scoring function (`calculate_match_score()`) to compare reported lost items with found items across four key attributes:

1. **Item Name**
2. **Category**
3. **Color**
4. **Location**

$$\text{Score} = \sum_{i \in \{\text{Name, Category, Color, Location}\}} \mathbb{I}(\text{lost}_i == \text{found}_i)$$

* **Score $\ge$ 2:** Displayed as a **Possible Match**.
* **Score = 4:** Classified as a **Strong Match**.

> **Design Choice:** A flexible score system was implemented over rigid exact-matching to account for human variance in item reporting while minimizing false negatives.

---

## 🚀 Getting Started

### Prerequisites

* Python 3.8 or higher installed on your system.

### Installation & Setup

1. **Clone the Repository:**
   ```bash
   git clone [https://github.com/your-username/unifind.git](https://github.com/your-username/unifind.git)
   cd unifind
