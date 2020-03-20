import http from "../../plugins/http";

/**
 * @author Kolynes Chinedu
 */
class SignInMixin {

    /**
     * Default constructor
     */
    constructor() {}

    /**
     * 
     */
    username : String;

    /**
     * 
     */
    password : String;

    /**
     * 
     */
    signingIn : Boolean;

    /**
     * 
     */
    errorMessage : String;

    /**
     * @return
     */
    async signIn() : Promise<Object> {
       this.signingIn = true;
       var returnObject = await http.getJSON("/sign-in/", {
           username: this.username,
           password: this.password
       }, "POST")
       this.signingIn = false;
        return returnObject;
    }   

}
export = SignInMixin;