import React from "react";
import './TableOrders.css'
// import Table from "react-bootstrap/Table";


export function TableOrders({orders}) {
    return (
        <table>
            <thead>
            <tr>
                <th>ID</th>
                <th>Placed</th>
                <th>Product Name</th>
                <th>Price</th>
                <th>First Name</th>
                <th>Last Name</th>
                <th>Address</th>
                <th>Email</th>
                <th>Status</th>
            </tr>
            </thead>
            <tbody>
            {orders.map(order => (
                <tr key={order.order_id}>
                    <td>{order.order_id}</td>
                    <td>{new Intl.DateTimeFormat("en-GB").format(new Date((order.order_placed)))}</td>
                    <td>
                        {new Intl.NumberFormat("en-GB", {
                            style: "currency",
                            currency: "GBP",
                            minimumFractionDigits: 0,
                            maximumFractionDigits: 2
                        }).format(order.price)}
                    </td>
                    <td>
                        {order.product_name}
                    </td>
                    <td>{order.first_name}</td>
                    <td>{order.last_name}</td>
                    <td>{order.address}</td>
                    <td>{order.email}</td>
                    <td>{order.order_status}</td>
                </tr>
            ))}
            </tbody>
        </table>
    );
}