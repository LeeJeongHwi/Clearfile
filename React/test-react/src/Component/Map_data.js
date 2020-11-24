/*global kakao */
import React ,{Component} from "react";
import axios from 'axios';
import SideDock from "./SideDock"
const { kakao } = window;
class Map_data extends Component{
    constructor(props){
        super(props);
        this.state = {
            markers : [],
            nextId : 0,
            map : null
        };
    }
    load_data = async () =>{  
        try {
            return await axios.post("http://localhost:8080/load_map")
        }catch(e){
            console.error(e);
        }
    };
    markInsert = async () => {
        const datas = (await this.load_data())['data'];
        datas.map(
            data => this.state.markers.push({
                id:data[0],
                name:data[1],
                lat:data[2],
                long:data[3]
            })
        )
        console.log("Marker Insert");
        return this.state.markers;
    }
    setMarker = async() => {
        const marker_List = await this.markInsert();
        marker_List.map(
            data => {
                const marker = new kakao.maps.Marker({
                    title : data['id'],
                    map : this.state.map,
                    position: new kakao.maps.LatLng(data["lat"],data["long"])
                })
                kakao.maps.event.addListener(marker,"click",function(){
                    console.log("Marker Click "+marker.getTitle())
                })
                marker.setMap(this.state.map)
                console.log("Marker Setting : "+data["name"]+" "+data["lat"]+" "+data["long"])
            }
        )
    }
    componentDidMount(){
        const script = document.createElement('script');
        script.async = true;
        script.src = "//dapi.kakao.com/v2/maps/sdk.js?appkey=c384f2a1aaa557ebd2e8e21d9c633dad"
        document.head.appendChild(script);
        
        script.onload = () => {
            kakao.maps.load(()=>{
                let el = document.getElementById('MyMap');
                this.setState({map:new kakao.maps.Map(el,{
                    center: new kakao.maps.LatLng(37.600, 126.955),
                    level:2
                })})
            })
        }
        this.setMarker();
    }
    render(){
        const mapStyle = {
            width : "100vw",
            height : "100vh"
        }
        return (
            <div id="MyMap" style={mapStyle}></div>
            
        )
    }
}
export default Map_data;