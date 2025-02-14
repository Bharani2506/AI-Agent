from langchain_google_genai import ChatGoogleGenerativeAI
from browser_use import Agent, Browser, BrowserConfig
from dotenv import load_dotenv
from pydantic import SecretStr
import os

load_dotenv()

import asyncio

task="""
### Updated Prompt for Shopping Agent – FC Barcelona Official Store Order (Search via Google)

**Objective:**  
Search for the **FC Barcelona Official Store** on Google, select the first relevant link, accept all cookies, set the language to **English**, set the region to **France**, navigate to the store, select a kit, and complete the order process without logging in.

**Important:**  
- Accept cookies if prompted.  
- Ensure the **language is set to English** and **region is set to France**.  
- Select the **first kit displayed** from the kits section.  
- Choose the **size M**.  
- Select the **player name "Pedri 8"** from the dropdown.  
- Proceed to checkout as a guest.

---

### Step 1: Search and Navigate to the Website
1. Open Google and search for **"FC Barcelona Official Store"**.  
2. Click on the first relevant link leading to the **official FC Barcelona store**.  
3. Accept all **cookies** if a popup appears.  
4. Change the website **language to English** and **region to France** if prompted.  

---

### Step 2: Navigate to Kits Section
1. On the main page, click on the **Shop** icon.  
2. Select the **"Kits"** option.  
3. Choose the **first product displayed** from the kits section.  

---

### Step 3: Customize the Kit
1. Select the **size as M**.  
2. Click on the **"Choose Player"** dropdown.  
3. Select **"Pedri 8"** from the available options.  

---

### Step 4: Add to Bag and Verify
1. Click on the **"View Bag"** option.  
2. Open the bag and verify that:  
   - The correct item (kit) is in the cart.  
   - The selected size is **M**.  
   - The chosen player customization is **Pedri 8**.  

---

### Step 5: Proceed to Checkout
1. Click on **"Continue with Payment"**.  
2. Check all details before proceeding.  
3. Ensure the order is correct and ready for checkout.

---

### Step 6: Confirm Order & Output Summary
- Once the order is placed, output a summary including:  
  - **Final item purchased** (FC Barcelona Kit - Pedri 8, Size M).  
  - **Total cost**.  

**Important:** Ensure efficiency and accuracy throughout the process.
"""

browser = Browser()
api_key_gemini = SecretStr(os.getenv('GEMINI_API_KEY') or 'your_api_key')

agent = Agent(
   task=task,
    llm=ChatGoogleGenerativeAI(model='gemini-2.0-flash-exp', api_key=api_key_gemini),
    browser=browser,
    )

async def main():
    await agent.run()
    input("Press Enter to close the browser...")
    await browser.close()

if __name__ == '__main__':
    asyncio.run(main())
