import http from "../../plugins/http";


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
    async sellValuable() : Promise<Object> {
        this.sellingValuable = true;
        var returnObject : Object = await http.getJSON("/sell-valuable/", {
            serial: this.serial,
            quantity: this.quantity
        }, "POST")
        this.sellingValuable = false;
        return returnObject;
    }

}
export = SellValuableMixin;