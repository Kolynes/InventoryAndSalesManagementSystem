package network;


/**
 * @author Kolynes Chinedu
 */
class LoadDemandsMixin {

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
    loadingDemands : Boolean;

    /**
     * 
     */
    page : Number;

    /**
     * @return
     */
    loadDemand() : Promise<Object> {
        // TODO implement here
        return null;
    }

}
export = LoadDemandsMixin;