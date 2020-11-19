import React , {Component,useState} from "react"
import ReactModal from "react-modal"

class modalTest extends Component{
    render(){
        return(
            <div>
                <ReactModal
                 isOpen={true}
                 shouldFocusAfterRender={true}
                 shouldCloseOnEsc={true}
                 contentLabel={"example Modal"}
                >TEST</ReactModal>
            </div>
        )
    }
}