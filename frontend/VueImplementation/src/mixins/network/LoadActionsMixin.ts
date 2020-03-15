package network;


/**
 * @author Kolynes Chinedu
 */
class LoadActionsMixin {

    /**
     * Default constructor
     */
    constructor() {}

    /**
     * 
     */
    from : Date;

    /**
     * 
     */
    to : Date;

    /**
     * 
     */
    loadingActions : Boolean;

    /**
     * 
     */
    page : Number;

    /**
     * @return
     */
    loadActions() : Promise<Object> {
        // TODO implement here
        return null;
    }

}
export = LoadActionsMixin;