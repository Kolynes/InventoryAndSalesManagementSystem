package network;


/**
 * @author Kolynes Chinedu
 */
class LoadValuablesMixin {

    /**
     * Default constructor
     */
    constructor() {}

    /**
     * 
     */
    valuableQuery : String;

    /**
     * 
     */
    loadingValuables : Boolean;

    /**
     * 
     */
    page : Number;

    /**
     * @return
     */
    loadValuables() : Promise<Object> {
        // TODO implement here
        return null;
    }

}
export = LoadValuablesMixin;