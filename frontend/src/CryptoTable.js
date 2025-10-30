import React, { useEffect, useCallback, useState } from 'react';
import './CryptoTable.css';

function CryptoTable(){
    //initializing state
    const [cryptoData, setCryptoData] = useState([]);

    const fetchData = useCallback(() => {
        fetch("http://127.0.0.1:5000/api/crypto/markets")
        .then(response => response.json())
        .then(data => {console.log(data); setCryptoData(data);})
        .catch(error => console.error("Error: Couldn't fetch crypto data: ", error));
    }, []);

    //loading jsonify data into state (JSON data -> list/array)
    useEffect(() => {
        fetchData();
        const interval = setInterval(fetchData, 60000);

        return () => clearInterval(interval);
    }, [fetchData]);

    //table formating
    return (
        <div>
            <button onClick={fetchData}>Refresh</button>
            <table>
                <thead>
                <tr>
                    <th>Name</th>
                    <th>Current Price</th>
                    <th>24h Change</th>
                </tr>
                </thead>
                <tbody>
                {
                    /*mapping out table */
                    cryptoData.map((coin) => (
                    <tr key={coin.id}>
                        <td>{coin.name}</td>
                        <td>{coin.current_price}</td>
                        <td className={coin.price_change_percentage_24h >= 0 ? "positive" : "negative"}>
                            {coin.price_change_percentage_24h.toFixed(2)}%
                        </td>
                    </tr>
                    ))
                }
                </tbody>
            </table>
        </div>
    );

}

export default CryptoTable;