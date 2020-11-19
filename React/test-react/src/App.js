import React,{Component} from 'react';
// import logo from './logo.svg';
import './App.css';
// import MyComponent from './MyComponent'
// import Counter from './Counter'
// import Say from './Say'
// import EventPractice from './EventPractice'
// import ValidationSample from "./ValidationSample"
// import ScrollBox from './ScrollBox';
// import IterationSample from './IterationSample';
import SideBarTest from "./SideBarTest";
import ReactDOM from "react-dom";
import Map_data from './Component/Map_data';
class App extends Component {
  render(){
    return(
      <div>
        <Map_data/>
      </div>
    )
  }
}

export default App;
