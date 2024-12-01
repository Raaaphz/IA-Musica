export const DashboardView = {
    getInputText() {
      return document.querySelector('#input-text').value.trim();
    },
    displayResult(message) {
      const resultDiv = document.querySelector('#result');
      resultDiv.textContent = message;
    },
    bindPredictButton(handler) {
      const predictButton = document.querySelector('#predict-btn');
      predictButton.addEventListener('click', handler);
    },
  };