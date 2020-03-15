package network;


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
    signUp() : Promise<Object> {
        // TODO implement here
        return null;
    }

}
export = SignUpMixin;