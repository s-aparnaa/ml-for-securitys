// app.js
// Secure Vibe Coding: Tokenization + Validation (No real card handling)

// Luhn algorithm for card number validation
function isValidCardNumber(number) {
  const cleaned = number.replace(/\D/g, "");
  let sum = 0;
  let shouldDouble = false;

  for (let i = cleaned.length - 1; i >= 0; i--) {
    let digit = parseInt(cleaned.charAt(i));
    if (shouldDouble) {
      digit *= 2;
      if (digit > 9) digit -= 9;
    }
    sum += digit;
    shouldDouble = !shouldDouble;
  }
  return sum % 10 === 0;
}

document.getElementById("payment-form").addEventListener("submit", function (e) {
  e.preventDefault();

  const cardNumber = document.getElementById("card-number").value;
  const expiry = document.getElementById("expiry").value;
  const cvv = document.getElementById("cvv").value;

  if (!isValidCardNumber(cardNumber)) {
    document.getElementById("result").innerText = "❌ Invalid card number (Luhn check failed)";
    return;
  }

  // Simulate tokenization (no sensitive info stored or sent)
  const token = "tok_" + Math.random().toString(36).substring(2, 16);

  document.getElementById("result").innerText =
    "✅ Tokenized Payment Info (simulated):\n" + token;
});
