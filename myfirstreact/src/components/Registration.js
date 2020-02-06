import React,{Component} from 'react';
import axios from 'axios';

export default class Registration extends Component {
    constructor(props){
        super(props);
        this.state = {
            Email:"",
            Password:"",
            Password_confirmation:"",
            Registration_Errors:""
        }
        this.handleSubmit=this.handleSubmit.bind(this);
        this.handleChange=this.handleChange.bind(this);
    }

    handleChange(event){
        this.setState({
            [event.target.name]:event.target.value
        });
    }

    handleSubmit(event){
        const {
            Email,
            Password,
            Password_confirmation
        } = this.state;

        axios.post("https://localhost:3001/registrations",
        {
            user: {
                Email:Email,
                Password:Password,
                Password_confirmation:Password
            }
        },
        {withCredentials:true}
        ).then(response => {
            console.log("registration result",response);
        })
        .catch(error=>{
            console.log("Registration error",error);
        });
        console.log("Submitted");
        event.preventDefault();
    }
    render() {
        return (
            <div>
                <form onSubmit={this.handleSubmit}>
                    <input 
                        type="email" 
                        name="Email" 
                        placeholder="Email" 
                        value={this.state.Email} 
                        onChange={this.handleChange} 
                        required>
                    </input>
                    <input 
                        type="password" 
                        name="Password" 
                        placeholder="Password" 
                        value={this.state.Password} 
                        onChange={this.handleChange} 
                        required>
                    </input>
                    <input 
                        type="password" 
                        name="Password_confirmation" 
                        placeholder="Password Confirmation" 
                        value={this.state.Password_confirmation} 
                        onChange={this.handleChange} 
                        required>
                    </input>

                    <button type="submit">Register</button>
                </form>
            </div>
        );
    }
}