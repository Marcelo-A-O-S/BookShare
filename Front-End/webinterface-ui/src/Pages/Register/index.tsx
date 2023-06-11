import {ChangeEvent, useState} from 'react'
import RegisterView from '../../ViewModel/RegisterView'


export default function Register(){
    const [register, setRegister] = useState<RegisterView >({
        firstname: "",
        lastname: "",
        email: "",
        password: "",
        passwordConfirm: "",
      });


    const OnChangeRegister = (event:ChangeEvent<HTMLInputElement>) =>{
        const { value, name } = event.target;
        if(name === "firstname"){
            setRegister(prevState =>({
                ...prevState,
                firstname: value
            }));
        }
        else if(name === "lastname"){
            setRegister(prevState =>({
                ...prevState,
                lastname: value
            }));
        }else if(name === "email"){
            setRegister(prevState =>({
                ...prevState,
                email: value
            }));
        }else if(name === "password"){
            setRegister(prevState =>({
                ...prevState,
                password: value
            }));
        }
        else if(name === "passwordConfirm"){
            setRegister(prevState =>({
                ...prevState,

                passwordConfirm: value
            }));
        }

    }
    async function Register(e:any){
        e.preventDefault();
        console.log(register);
        const response =  await fetch("http://127.0.0.1:5000//Register", {
            method:"POST",
            headers: {
                "Content-Type": "application/json",
              },
            body: JSON.stringify(register),
         })
        const result = await response.json();
        console.log(result)
        console.log(result.status)
    }
    return(
        <>
        <form>
            <div>
                <label>First Name</label>
                <input type="text" name="firstname" id=""
                value={register.firstname}
                onChange={(e) => OnChangeRegister(e)} required/>
            </div>
            <div>
                <label>Last Name</label>
                <input type="text" name="lastname" id=""
                value={register.lastname}
                onChange={(e) => OnChangeRegister(e)} required/>
            </div>
            <div>
                <label>Email</label>
                <input type="text" name="email" id=""
                value={register.email}
                onChange={(e) => OnChangeRegister(e)} required/>
            </div>
            <div>
                <label>Password</label>
                <input type={"text"} name="password" id=""
                value={register.password}
                onChange={(e) => OnChangeRegister(e)} required/>
            </div>
            <div>
                <label>Confirm Password</label>
                <input type={"text"} name="passwordConfirm" id=""
                value={register.passwordConfirm}
                onChange={(e) => OnChangeRegister(e)} required/>
            </div>

            <button type={"button"} onClick={(e)=>Register(e)}>Registrar</button>
        </form>
        </>
    )
}
