package network;


/**
 * @author Kolynes Chinedu
 */
class DestockValuableMixin {

    /**
     * Default constructor
     */
    constructor() {}

    /**
     * 
     */
    stock : String;

    /**
     * 
     */
    serial : String;

    /**
     * 
     */
    destockingValuable : Boolean;

    /**
     * @return
     */
    destockValuable() : Promise<Object> {
        // TODO implement here
        return null;
    }

}
export = DestockValuableMixin;