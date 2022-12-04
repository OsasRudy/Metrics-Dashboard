import './MetricCard.css'
import {Icon} from '@iconify/react';

const MetricCard = ({title, value, color, png}) => {


    return (
        <div className="parentContainer">
            <div className="CompactCard" style={color}>
                <div className="iconDisplay">
                    <Icon icon={png} width={43}></Icon>
                    <span>{title}</span>

                </div>
                <div className="detail">
                    <span>{value}</span>
                </div>
            </div>
        </div>
    )
}

export default MetricCard