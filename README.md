# Pybot
Python Chatbot that operates from a terminal.
Pybot may make mistakes, so think critically, and double check info.
Pybot is a work in progress, so it may not be perfect.

## Installation
To install the required packages, run:
```
pip install -r requirements.txt
```
Using `rich` for markdown translator.
Using `azure-ai-inference` for SDK.

## Models
Pybot uses the following models:
- `OpenAI GPT-4o-mini`
- `Meta Llama-3.3-70B-Instruct`
- `OpenAI GPT-4o`
- `Mistral-small`
- `Phi-4 multimodal-instruct`
  
Powered by Github Models


## Usage
To start the chatbot, run the following command:
```
python pybot/main.py
```
## Examples
To see example converations, see `log.txt`:
```
2025-03-04 16:45:55 - User input: what is the quadratic equation?
2025-03-04 16:45:59 - Bot response: The **quadratic equation** is a type of polynomial equation of degree 2 and is generally written in the standard form:

\[
ax^2 + bx + c = 0
\]

Here:
- \(x\) represents the variable or unknown,
- \(a\), \(b\), and \(c\) are constants (numbers), where \(a \neq 0\) (if \(a = 0\), it's not quadratic!).

### Solving a Quadratic Equation
Quadratic equations can be solved using a variety of methods, including:
1. **Factoring** (if possible),
2. **Completing the square**,
3. The **Quadratic Formula**:
   \[
   x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
   \]
   - The term under the square root \(b^2 - 4ac\) is called the **discriminant** and determines the nature of the roots.

### Examples:
1. \(x^2 - 5x + 6 = 0\): Factoring gives \((x - 2)(x - 3) = 0\), so \(x = 2\) or \(x = 3\).
2. \(2x^2 + 4x - 6 = 0\): Use the Quadratic Formula to find the solutions.

### Applications 🧠✨
Quadratic equations show up in many areas, such as:
- Physics (e.g., projectile motion 🏀),
- Engineering 📐,
- Economics 📊 (profit maximization),
- And much more!

Let me know if you'd like a specific example solved step by step! 😊
```
