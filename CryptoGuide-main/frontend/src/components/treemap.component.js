import React, { Component } from 'react';
import * as d3 from 'd3';
import './TreeMapComponent.css'; // Ensure this file contains your styles

export default class TreeMapComponent extends Component {
  state = {
    data: null // Initialize state to hold the fetched data
  };

  componentDidMount() {
    this.fetchData();
  }

  async fetchData() {
    try {
      const response = await fetch('http://localhost:5000/cryptos');
      const jsonData = await response.json();
      const transformedData = this.transformData(jsonData);
      this.setState({ data: transformedData }, this.drawTreeMap);
    } catch (error) {
      console.error("Failed to fetch data: ", error);
    }
  }

  transformData(jsonData) {
    return {
      name: "Crypto",
      children: jsonData.map(item => ({
        name: item.crypto,
        value: item.score
      }))
    };
  }

  drawTreeMap() {
    if (!this.state.data) return;

    const container = d3.select(this.refs.treeMap).classed("tree-map-container", true);
    container.selectAll("*").remove();

    const data = this.state.data;
    const root = d3.hierarchy(data).sum(d => d.value);
    d3.treemap().size([1200, 520])(root);

    const svg = container.append("svg")
      .attr("width", 1200)
      .attr("height", 520)
      .attr("class", "tree-map-svg");

    const values = root.leaves().map(d => d.data.value);
    const minValue = d3.min(values);
    const maxValue = d3.max(values);

    // Adjust the color scale to be more dynamic
    const colorScale = d3.scaleSequential([minValue, maxValue], d3.interpolateViridis);

    const nodes = svg.selectAll("g")
      .data(root.leaves())
      .enter()
      .append("g")
      .attr("class", "tree-node")
      .attr("transform", d => `translate(${d.x0},${d.y0})`);

    nodes.append("rect")
      .attr("id", d => d.data.name)
      .attr("width", d => d.x1 - d.x0)
      .attr("height", d => d.y1 - d.y0)
      .attr("fill", d => colorScale(d.data.value))
      .attr("class", "rect-hover")
      .on("mouseover", (event, d) => {
        const tooltip = d3.select(".tooltip");
        tooltip.transition().duration(200).style("opacity", 0.9);
        tooltip.html(`${d.data.name}: ${d.data.value}`)
          .style("left", (event.pageX) + "px")
          .style("top", (event.pageY - 28) + "px");
      })
      .on("mouseout", () => {
        const tooltip = d3.select(".tooltip");
        tooltip.transition().duration(500).style("opacity", 0);
      });

    nodes.append("text")
      .attr("clip-path", d => `url(#clip-${d.data.name})`)
      .selectAll("tspan")
      .data(d => d.data.name.split(/(?=[A-Z][^A-Z])/g))
      .enter().append("tspan")
      .attr("x", 4)
      .attr("y", (d, i) => 13 + i * 10)
      .text(d => d);

    if (d3.select("body").select(".tooltip").empty()) {
      d3.select("body").append("div")
        .attr("class", "tooltip")
        .style("opacity", 0);
    }

    window.addEventListener("resize", this.drawTreeMap.bind(this));
  }

  componentWillUnmount() {
    window.removeEventListener("resize", this.drawTreeMap.bind(this));
  }

  render() {
    return <div ref="treeMap" />;
  }
}
