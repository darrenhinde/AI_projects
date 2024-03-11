import React, { Component } from 'react';
import './Summarizer.css'; // Import CSS file for styling

export default class Summarizer extends Component {
    state = {
        summaries: [] // Initialize state to hold fetched data
    };

    componentDidMount() {
        this.fetchSummaries();
    }

    async fetchSummaries() {
        try {
            const response = await fetch('http://localhost:5000/summaries');
            const data = await response.json();
            this.setState({ summaries: data });
        } catch (error) {
            console.error("Failed to fetch summaries: ", error);
        }
    }

    render() {
        const { summaries } = this.state;
        return (
            <div className="summarizer-container">
                <h2>Trending Crypto Videos</h2>
                <table>
                    <tbody>
                        <tr>
                            <th>Videos</th>
                            <th>Link</th>
                            <th>Summary of Video</th> {/* New column */}
                        </tr>
                        {summaries.map(summary => (
                            <tr key={summary._id}>
                                <td>{summary.title}</td>
                                <td><a href={`https://youtube.com/watch?v=${summary.id}`} target="_blank" rel="noopener noreferrer">Watch</a></td>
                                <td>{summary.summary}</td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>
        );
    }
}
