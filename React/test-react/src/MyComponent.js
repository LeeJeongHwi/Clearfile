import React, {Component} from "react";
import PropTypes from "prop-types"

// const MyComponent = ({name,children,favoriteNumber}) =>{
//     return (
//         <div>
//             <h1>Hello My name is {name}</h1>
//             <h2>Children Value : {children}</h2>
//             <h3>My Favorite Number : {favoriteNumber}</h3>
//         </div>
//     )
// };
// MyComponent.defaultProps = {
//     name : "Base Name"
// };
// MyComponent.propTypes = {
//     name : PropTypes.string,
//     favoriteNumber : PropTypes.number.isRequired
// }
class MyComponent extends Component {
    render(){
        const { name, favoriteNumber,children} = this.props;
        return (
            <div>
                <h1>{name}</h1>
                <h2>{children}</h2>
                <h3>{favoriteNumber}</h3>
            </div>
        );
    }
}
MyComponent.defaultProps = {
    name : "Base Name"
};

MyComponent.propTypes = {
    name : PropTypes.string,
    favoriteNumber : PropTypes.number.isRequired
};

export default MyComponent;