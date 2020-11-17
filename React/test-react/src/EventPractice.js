import React , {Component,useState} from "react";

const EventPractice = () =>{
    const [username,setUsername] = useState('');
    const [message,setMessage] = useState('');
    const onChangeUsername = e => setUsername(e.target.value);
    const onChangeMessage = e => setMessage(e.target.value);
    const onClick = () => {
        alert(username+ ': '+ message);
        setUsername('');
        setMessage('');
    };
    const onKeyPress =e => {
        if (e.key === "Enter"){
            onClick();
        }
    };
    return (
        <div>
            <h1>Event Practice</h1>
            <input
             type = 'text'
             name = 'username'
             placeholder = 'User_Name'
             value ={username}
             onChange={onChangeUsername}></input>
             <input
              tpye='text'
              name = 'message'
              placeholder='input anyone'
              value ={message}
              onChange={onChangeMessage}
              onKeyPress={onKeyPress}></input>
            <button onClick={onClick}>Check!</button>
        </div>
    );
};

export default EventPractice;