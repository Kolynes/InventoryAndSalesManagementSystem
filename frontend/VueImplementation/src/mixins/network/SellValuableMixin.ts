package network;


/**
 * @author Kolynes Chinedu
 */
class SellValuableMixin {

    /**
     * Default constructor
     */
    constructor() {}

    /**
     * 
     */
    serial : String;

    /**
     * 
     */
    quantity : Number;

    /**
     * 
     */
    sellingValuable : Boolean;

    /**
     * @return
     */
    sellValuable() : Promise<Object> {
        // TODO implement here
        return null;
    }

}
export = SellValuableMixin;