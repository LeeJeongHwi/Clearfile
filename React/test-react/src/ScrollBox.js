import React , {Component} from "react";

class ScrollBox extends Component{
    scrollToBottom = () => {
        const { scrollHeight, clientHeight} = this.box;

        this.box.scrollTop = scrollHeight - clientHeight;
    }
    render(){
        const style ={
            border : "1px solid black",
            height : "300px",
            width : "300px",
            overflow : "auto", // 스크롤 
            position : "relative" // Position
        };
        const innerStyle = {
            width : "100%",
            height : "650px",
            background : "linear-gradient(white,black)"
        }
        return (
            <div
             style = {style}
             ref = {(ref)=>{this.box=ref}}>
             <div style={innerStyle}/>
             </div>
        )
    }
}

export default ScrollBox;