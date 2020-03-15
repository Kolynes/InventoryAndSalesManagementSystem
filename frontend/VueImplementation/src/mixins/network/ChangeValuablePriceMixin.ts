import http from "../../plugins/http";


/**
 * @author Kolynes Chinedu
 */
class ChangeValuablePriceMixin {

    /**
     * Default constructor
     */
    constructor() {}

    /**
     * 
     */
    price : Number;

    /**
     * 
     */
    serial : String;

    /**
     * 
     */
    changingValuablePrice : Boolean;

    /**
     * @return
     */
    async changeValuablePrice() : Promise<Object> {
        this.changingValuablePrice = true;
        var returnObject : Object = await http.getJSON("/stock-valuable/", {
            serial: this.serial,
            price: this.price
        }, "POST")
        this.changingValuablePrice = false;
        return returnObject;
    }

}
export = ChangeValuablePriceMixin;