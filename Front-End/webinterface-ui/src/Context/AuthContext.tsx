import React, {createContext , useState , useEffect} from "react";
import User from "../Models/User";
import IUser from "../Interfaces/IUser";

interface AuthUser {
    user: IUser | null,
    signed: boolean,
    SignIn(BodyUser:object): Promise<void>,
    VerificarUsuario(): void,
    SignOut():void
}


const AuthContext = createContext<AuthUser>({} as AuthUser);



export const AuthProvider = ({ children }: any) => {
    const [user, setUser] = useState<IUser|null>({} as IUser)
    const [signed, setSigned] = useState<boolean>(false)

    useEffect(()=>{
        async function VerificarAutenticacao(){
            const UserStorage = localStorage.getItem("user");
            if(UserStorage){
                setUser(JSON.parse(UserStorage))
                setSigned(true)
            }
        }
        VerificarAutenticacao()

    },[])
    async function VerificarUsuario(){
        console.log(user)
        console.log(signed)
    }
    async function SignIn(BodyUser:User){
        setUser(BodyUser);
        setSigned(true);
        localStorage.setItem("user", JSON.stringify(BodyUser))

    }
    async function SignOut(){
        setUser(null);
        setSigned(false);
        localStorage.removeItem("user")
        localStorage.clear()

    }
    return(
        <AuthContext.Provider value={{ signed: signed, user: user, SignIn, VerificarUsuario, SignOut }}>
            {children}
        </AuthContext.Provider>
    )
}

export default AuthContext
