import http from "../../plugins/http";

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
    async destockValuable() : Promise<Object> {
        this.destockingValuable = true;
        var returnObject : Object = await http.getJSON("/destock-valuable/", {
            seral: this.serial,
            stock: this.stock
        }, "POST")
        this.destockingValuable = false;
        return returnObject;
    }

}
export = DestockValuableMixin;