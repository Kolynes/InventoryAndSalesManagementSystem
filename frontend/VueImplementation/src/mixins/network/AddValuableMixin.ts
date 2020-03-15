import http from "../../plugins/http";

/**
 * @author Kolynes Chinedu
 */
class AddValuableMixin {

    /**
     * Default constructor
     */
    constructor() {}

    /**
     * 
     */
    name : String;

    /**
     * 
     */
    price : Number;

    /**
     * 
     */
    addingValuable : Boolean;

    /**
     * @return
     */
    async addValuable() : Promise<Object> {
        this.addingValuable = true;
        var returnObject = await http.getJSON("/add-valuable/", {
            name: this.name,
            price: this.price
        }, "POST")
        this.addingValuable = false;
        return returnObject;
    }

}
export = AddValuableMixin;