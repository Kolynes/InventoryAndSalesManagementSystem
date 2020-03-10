<?php

namespace App;

use Illuminate\Database\Eloquent\Model;

class Valuable extends Model
{
    public function transactions(){
        return $this->hasMany('App\Transaction');
    }

    public function demands(){
        return $this->hasMany('App\Demand');
    }
}
