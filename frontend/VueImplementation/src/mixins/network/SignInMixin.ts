package network;


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
    signingIn : Password;

    /**
     * 
     */
    errorMessage : String;

    /**
     * @return
     */
    signIn() : Promise<Object> {
        // TODO implement here
        return null;
    }

}
export = SignInMixin;