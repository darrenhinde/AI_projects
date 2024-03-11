import React, { Component } from 'react';
import axios from 'axios'; // Import Axios
import './Summarizer.css'; // Import CSS file for styling

export default class Summarizer extends Component {
    state = {
        cryptos: [] // Initialize state to hold cryptocurrency data
    };

    componentDidMount() {
        this.fetchCryptos();
    }

    fetchCryptos = () => {
        // Use Axios to fetch data from your API endpoint
        axios.get('http://localhost:5000/cryptos')
            .then(response => {
                // Update state with fetched cryptocurrency data
                this.setState({ cryptos: response.data });
            })
            .catch(error => {
                console.error("There was an error fetching the crypto data: ", error);
            });
    };

    render() {
        return (
            <div className="summarizer-container">
                <h2>Daily Investment Summarization</h2>
                <table>
                    <tbody>
                        <tr>
                            <th>Asset</th>
                            <th>Summary</th>
                        </tr>
                        {
                            // Map over cryptos in state to create a table row for each
                            this.state.cryptos.map(crypto => (
                                <tr key={crypto._id}>
                                    <td>{crypto.crypto}</td>
                                    <td>Views: {crypto.views}, Score: {crypto.score}</td>
                                </tr>
                            ))
                        }
                    </tbody>
                </table>
            </div>
        );
    }
}
