import React,{Component} from 'react';
import logo from './logo.svg';
import './App.css';
import MyComponent from './MyComponent'
import Counter from './Counter'
import Say from './Say'
import EventPractice from './EventPractice'
import ValidationSample from "./ValidationSample"
import ScrollBox from './ScrollBox';
import IterationSample from './IterationSample';
// const App = () =>{
//   // return (
//   // <MyComponent name = "Leepapers" favoriteNumber={3}>
//   //   React
//   // </MyComponent>
//   // )
//   // return <Counter />
//   // return <Say />;
//   // return <EventPractice />;
//   return <ValidationSample />
// }

class App extends Component {
  render(){
    // return (
    //   <ValidationSample />
    // );
    // return(
    //   <div>
    //     <ScrollBox ref={(ref) => this.scrollBox=ref}/>
    //     {/* ref:DOM , scrollBox의 위치를 toBottom으로.. */}
    //     <button onClick={()=> this.scrollBox.scrollToBottom()}>
    //       to Bottom
    //     </button>
    //   </div>
    // )
    return(<IterationSample/>);
  }
}

export default App;
