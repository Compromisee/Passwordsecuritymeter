

---

# Password Strength Analyzer 🔐

A Python-based terminal tool that evaluates password strength using a custom scoring algorithm. It checks for special characters, rare letters, length penalties, and even uses natural language processing to detect "real words" within your password.

## ✨ Features

*   **Dynamic Scoring:** Real-time point updates as the script parses your input.
*   **Dictionary Detection:** Uses `wordninja` and `nltk` to identify dictionary words, rewarding memorable phrase-based passwords.
*   **Visual Feedback:** Colorful terminal output powered by `colorama`.
*   **Smart Penalties:** Deducts points for "over-stuffing" (too many numbers or symbols) to encourage balanced security.
*   **Big Result Energy:** Displays your final score in a massive `ansi_shadow` ASCII banner using `pyfiglet`.

## 🚀 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Compromisee/Passwordsecuritymeter.git
   cd password-analyzer
   ```

2. **Install dependencies:**
   ```bash
   pip install colorama nltk pyfiglet wordninja
   ```

3. **Download NLTK Data:**
   The script will automatically attempt to download the necessary word corpora on the first run.

## 🛠️ How It Works

The script evaluates strength based on several criteria:

| Criteria | Reward/Penalty |
| :--- | :--- |
| **Special Characters** | +5 points each (up to 4) |
| **Standard Letters** | +1 point per character |
| **Rare Letters** | +3 points for characters like `z, q, x, j, k, v, b, p, y, g` |
| **Length** | Bonuses for 14+ chars; scaling penalties for excessive length (15+) |
| **Real Words** | +3 points for every real English word detected |
| **Complexity Overload** | Severe point deductions if you use >4 numbers or >4 symbols |

## 💻 Usage

Run the script directly from your terminal:
```bash
python main.py
```

Follow the prompt to enter your password. The script will clear the screen with a scrolling effect and display your final calculated score.

## 📦 Dependencies

*   [colorama](https://pypi.org/project/colorama/) - Cross-platform colored terminal text.
*   [pyfiglet](https://pypi.org/project/pyfiglet/) - ASCII art text generation.
*   [wordninja](https://pypi.org/project/wordninja/) - Probabilistically split concatenated words.
*   [nltk](https://pypi.org/project/nltk/) - Natural Language Toolkit for English word validation.

---

### ⚠️ Note
*This tool is intended for educational purposes and provides a "strength score" based on custom logic. It should not be used as a definitive measurement of cryptographic security.*
```
