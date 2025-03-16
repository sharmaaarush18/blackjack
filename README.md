# Blackjack Game (Python)  

## Introduction  
This is a simple **text-based Blackjack game** implemented in Python. You play against the computer, trying to get as close to **21** as possible without going over. The game follows standard Blackjack rules, including **hitting, standing, and handling Aces dynamically**.  

## Features  
- ✅ **Play against the computer** with automatic dealer logic.  
- ✅ **Aces automatically adjust** from 11 to 1 if necessary to avoid busting.  
- ✅ **Dealer follows standard Blackjack rules** (hits until at least 17).  
- ✅ **Clean and readable code**, structured with functions.  

## How to Play  
1. The game starts by dealing **two cards** to you and the dealer.  
2. You can choose to:  
   - **Hit (`y`)** → Take another card.  
   - **Stand (`n`)** → Keep your current hand.  
3. If your total goes **above 21**, you lose automatically.  
4. After you stand, the **dealer will draw cards** until reaching **17 or higher**.  
5. The game then compares scores and **determines the winner**.  

## Winning Conditions  
🎉 **You win if:**  
✅ You get **21** with two cards → **Blackjack!**  
✅ The **dealer goes over 21** (busts).  
✅ Your score is **higher than the dealer’s**.  

😢 **You lose if:**  
❌ You go **over 21** (bust).  
❌ The **dealer’s score is higher than yours**.  

🤝 **It's a draw if:**  
🔹 Both scores are **the same**.  

## How to Run the Game  
1. Ensure you have **Python 3** installed on your system.  
2. Download the script or copy it into a Python file (`blackjack.py`).  
3. Run the script in your **terminal or command prompt**:  

   ```sh
   python blackjack.py
