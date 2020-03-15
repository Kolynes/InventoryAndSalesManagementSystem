import http from "../../plugins/http";


/**
 * @author Kolynes Chinedu
 */
class StockValuableMixin {

    /**
     * Default constructor
     */
    constructor() {}

    /**
     * 
     */
    stock : Number;

    /**
     * 
     */
    serial : String;

    /**
     * 
     */
    stockingValuable : Boolean;

    /**
     * @return
     */
    async stockValuable() : Promise<Object> {
        this.stockingValuable = true;
        var returnObject : Object = await http.getJSON("/stock-valuable/", {
            seral: this.serial,
            stock: this.stock
        }, "POST")
        this.stockingValuable = false;
        return returnObject;
    }

}
export = StockValuableMixin;