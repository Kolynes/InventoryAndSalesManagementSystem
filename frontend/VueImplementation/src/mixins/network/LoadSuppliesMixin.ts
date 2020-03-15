package network;


/**
 * @author Kolynes Chinedu
 */
class LoadSuppliesMixin {

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
    loadingSupplies : Boolean;

    /**
     * 
     */
    page : Number;

    /**
     * @return
     */
    loadSupplies() : Promise<Object> {
        // TODO implement here
        return null;
    }

}
export = LoadSuppliesMixin;