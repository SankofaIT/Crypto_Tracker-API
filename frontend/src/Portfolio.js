import React, { useState, useEffect } from "react";

function Portfolio() {
  const [portfolio, setPortfolio] = useState([]);
  const [coin, setCoin] = useState("");
  const [amount, setAmount] = useState("");

  // Load saved portfolio data from local storage
  useEffect(() => {
    const savedPortfolio = JSON.parse(localStorage.getItem("portfolio")) || [];
    setPortfolio(savedPortfolio);
  }, []);

  // Save to local storage whenever portfolio changes
  useEffect(() => {
    localStorage.setItem("portfolio", JSON.stringify(portfolio));
  }, [portfolio]);

  // Add a new coin
  const addCoin = () => {
    if (coin && amount) {
      const newEntry = { coin, amount: parseFloat(amount) };
      setPortfolio([...portfolio, newEntry]);
      setCoin("");
      setAmount("");
    }
  };

  // Remove a coin
  const removeCoin = (index) => {
    const updated = portfolio.filter((_, i) => i !== index);
    setPortfolio(updated);
  };

  return (
    <div className="portfolio">
      <h2>My Portfolio</h2>

      <div className="input-section">
        <input
          type="text"
          placeholder="Coin name (e.g. Bitcoin)"
          value={coin}
          onChange={(e) => setCoin(e.target.value)}
        />
        <input
          type="number"
          placeholder="Amount owned"
          value={amount}
          onChange={(e) => setAmount(e.target.value)}
        />
        <button onClick={addCoin}>Add Coin</button>
      </div>

      <table>
        <thead>
          <tr>
            <th>Coin</th>
            <th>Amount</th>
            <th>Remove</th>
          </tr>
        </thead>
        <tbody>
          {portfolio.map((entry, index) => (
            <tr key={index}>
              <td>{entry.coin}</td>
              <td>{entry.amount}</td>
              <td>
                <button onClick={() => removeCoin(index)}>X</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default Portfolio;
