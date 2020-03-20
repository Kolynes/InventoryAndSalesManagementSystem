import http from "../../plugins/http";

/**
 * @author Kolynes Chinedu
 */
class SignUpMixin {

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
    email : String;

    /**
     * 
     */
    password : String;

    /**
     * 
     */
    name : String;

    /**
     * 
     */
    signingUp : Boolean;

    /**
     * 
     */
    errorMessages : Object;

    /**
     * @return
     */
    async signUp() : Promise<Object> {
        this.signingUp = true;
        var returnObject =  await http.getJSON("/sign-up/", {
            username: this.username,
            email: this.email,
            password: this.password,
            name: this.name
        }, "POST")
        this.signingUp = false;
        return returnObject;
    }

}
export = SignUpMixin;