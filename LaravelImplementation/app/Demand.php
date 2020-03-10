<?php

namespace App;

use Illuminate\Database\Eloquent\Model;

class Demand extends Model
{
    public function valuable(){
        return $this->belongsTo('App\Valuable');
    }
}
