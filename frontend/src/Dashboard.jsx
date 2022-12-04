import React, {Component, useEffect, useState} from 'react';
import './Dashboard.css'
import {TableOrders} from "./components/TableOrders/TableOrders";
import axios from "axios";
import MetricCard from "./components/MetricCard/MetricCard";
import chartBar from '@iconify/icons-uil/chart-bar';
import PoundCircle from '@iconify/icons-uil/pound-circle'
import Package from '@iconify/icons-uil/package'
import InfoCircle from '@iconify/icons-uil/info-circle'

let metricsData = {}


export let metric_total_order = 0
export let metric_monthly_order = 0
export let metric_orders_in_progress = 0
export let metric_revenue = 0
export let metric_recent_orders = []
const Dashboard = () => {
    const  [metrics, setMetrics] = useState([]);
    useEffect(() => {
        axios.get('/api').then(res => setMetrics(res.data));
    }, []);

    //metrics is the array


    metricsData = metrics.map((metric, index) => {
        < p key={index}></p>
        metric_total_order = metric.total_orders;
        metric_monthly_order = metric.total_monthly_orders;
        metric_orders_in_progress = metric.total_orders_in_progress;
        metric_revenue = metric.revenue;
        metric_recent_orders = metric.recent_orders;


    })
    const metric_revenue_format = new Intl.NumberFormat("en-GB", {
        style: "currency",
        currency: "GBP",
        minimumFractionDigits: 0,
        maximumFractionDigits: 2
    }).format(metric_revenue)

    return (
        <div className="Dashboard">
            <h1> Metrics Dashboard </h1>

            <div className="metricDisplay">
            <MetricCard
                title={"Total Orders"}
                value={metric_total_order}
                png={InfoCircle}
                color={{background:'linear-gradient(180deg, #bb67ff 0%, #c484f3 100%)',
                    boxShadow: "0px 10px 20px 0px #e0c6f5"}}
            />
            <MetricCard
                title={"Monthly Orders"}
                value={metric_monthly_order}
                png={chartBar}
                color={{background:'linear-gradient(180deg, #FF919D 0%, #FC929D 100%)',
                    boxShadow: "0px 10px 20px 0px #FDC0C7"}}
            />
            <MetricCard
                title={"Orders in Progress"}
                value={metric_orders_in_progress}
                png={Package}
                color={{background:'linear-gradient(rgb(248, 212, 154) -146.42%, rgb(255 202 113) -46.42%)',
                    boxShadow:"0px 10px 20px 0px #FDC0C7"}}
            />
            <MetricCard
                title={"Revenue"}
                value={metric_revenue_format}
                png={PoundCircle}
                color={{background:'linear-gradient(180deg, #00bfff 0%, #00bfff 100%)',
                    boxShadow:"0px 10px 20px 0px #FDC0C7"}}
            />
            </div>
            <h3> Recent Orders</h3>
            <TableOrders orders={metric_recent_orders}/>
        </div>

    );
}

export default Dashboard

