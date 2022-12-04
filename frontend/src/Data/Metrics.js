import {useEffect, useState} from "react";
import axios from "axios";

let defaultMetrics = {
    totalOrders: 0,
    totalOrdersThisMonth: 0,
    totalOrdersInProgress: 0,
    revenue: 0,
    expectedRevenue: 0,
    recentOrders: []
}

export let metric_total_orders = 0
export let data_total_orders = metric_total_orders
export function Metrics() {


    const  [metrics, setMetrics] = useState([]);
    useEffect(() => {
        axios.get('/dashboard').then(res => setMetrics(res.data));
    }, []);

    //metrics is the array



    // defaultMetrics = metrics.map((metric, index) => {
    //     < p key={index}></p>
    //     metric_total_orders = metric.total_orders
    //
    // })

    // console.log('1',metric_total_orders)

    return metrics.map((p, index) => {

        return <p key={index}>{p.total_orders} {p.total_monthly_orders} {p.total_orders_in_progress} {p.revenue} </p>
    })
}
