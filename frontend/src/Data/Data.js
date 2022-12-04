import {
    UilChartBar,
    UilPoundCircle,
    UilPackage,
    UilInfoCircle
} from "@iconscout/react-unicons";

import {useEffect, useState} from "react";
import axios from "axios";
import {metric_total_orders} from "./Metrics";
import {metric_total_order} from "../Dashboard";

let defaultMetrics = {
    totalOrders: 0,
    totalOrdersThisMonth: 0,
    totalOrdersInProgress: 0,
    revenue: 0,
    expectedRevenue: 0,
    recentOrders: []
}


// import metrics from './Metrics'


// export function Data() {
//
//
//     const [metrics, setMetrics] = useState([]);
//     useEffect(() => {
//         axios.get('/dashboard').then(res => setMetrics(res.data));
//     }, []);
//
//     //metrics is the array
//     console.log('1', metric_total_orders)
//
//     return metrics.map((p, index) => {
//
//         return <p key={index}>{p.total_orders} {p.total_monthly_orders} {p.total_orders_in_progress} {p.revenue} </p>
//     })
// }


// Metrics Cards Data
export const cardsData = [
    {
        title: "Total Orders",
        color: {
            backGround: "linear-gradient(180deg, #bb67ff 0%, #c484f3 100%)",
            boxShadow: "0px 10px 20px 0px #e0c6f5",
        },
        barValue: 70,
        value: 1000,
        png: UilInfoCircle,
        series: [
            {
                name: "Sales",
                data: [31, 40, 28, 51, 42, 109, 100],
            },
        ],
    },
    {
        title: "Monthly Orders",
        color: {
            backGround: "linear-gradient(180deg, #FF919D 0%, #FC929D 100%)",
            boxShadow: "0px 10px 20px 0px #FDC0C7",
        },
        barValue: 70,
        value: 0,
        png: UilChartBar,
        series: [
            {
                name: "Sales",
                data: [31, 40, 28, 51, 42, 109, 100],
            },
        ],

    },
    {
        title: "Orders in Progress",
        color: {
            backGround:
                "linear-gradient(rgb(248, 212, 154) -146.42%, rgb(255 202 113) -46.42%)",
            boxShadow: "0px 10px 20px 0px #F9D59B",
        },
        barValue: 70,
        value: 0,
        png: UilPackage,
        series: [
            {
                name: "Sales",
                data: [31, 40, 28, 51, 42, 109, 100],
            },
        ],

    },
    {
        title: "Revenue",
        color: {
            backGround: "linear-gradient(180deg, #00bfff 0%, #00bfff 100%)",
            boxShadow: "0px 10px 20px 0px #e0c6f5",
        },
        barValue: 70,
        value: 0,
        png: UilPoundCircle,
        series: [
            {
                name: "Sales",
                data: [31, 40, 28, 51, 42, 109, 100],
            },
        ],


    },
];

console.log(defaultMetrics.total_orders)

// defaultMetrics = metrics.map((metric, index) => {
//     < p key={index}>
//         defaultMetrics.total_orders = metric.total_orders</p>
//
// })
