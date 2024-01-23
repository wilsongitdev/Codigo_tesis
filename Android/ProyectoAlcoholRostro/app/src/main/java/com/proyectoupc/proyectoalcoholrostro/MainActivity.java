package com.proyectoupc.proyectoalcoholrostro;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.util.Log;
import android.view.KeyEvent;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import com.android.volley.Cache;
import com.android.volley.Network;
import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.BasicNetwork;
import com.android.volley.toolbox.DiskBasedCache;
import com.android.volley.toolbox.HurlStack;
import com.android.volley.toolbox.StringRequest;
import com.google.gson.JsonObject;
import com.google.gson.JsonParser;
import com.proyectoupc.proyectoalcoholrostro.JavaActivities.User.ListUserAlcoholMeasure;

import java.io.UnsupportedEncodingException;
import java.util.HashMap;
import java.util.Map;

public class MainActivity extends AppCompatActivity {
    EditText username,password;
    Button btnloggin;
    SharedPreferences sharedPref;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        getSupportActionBar().hide();//ocultar barra de action/menu
        sharedPref = getSharedPreferences("LogginData",Context.MODE_PRIVATE);

        if (sharedPref.getBoolean("IsLogged",false)){//esta logeado
            Intent intloggin = new Intent(getApplicationContext(), ListUserAlcoholMeasure.class);
            startActivity(intloggin);
        }
        else{// no se logeo
            setContentView(R.layout.activity_main);
            //ocultar la barra de acción/menu del mennú principal

            username = findViewById(R.id.edtEmailAddress);
            password = findViewById(R.id.edtTextPassword);
            btnloggin = findViewById(R.id.buttonloggin);

            btnloggin.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View vi) {
                    btnloggin.setEnabled(false);
                    RequestQueue requestQueue;
                    Cache cache = new DiskBasedCache(getCacheDir(), 1024 * 1024); // 1MB cap
                    Network network = new BasicNetwork(new HurlStack());
                    requestQueue = new RequestQueue(cache, network);
                    requestQueue.start();
                    StringRequest strrequest=new StringRequest(Request.Method.POST, Constants.url_api + "/proy_control_alc/login/signinuser.php",
                            new Response.Listener<String>() {
                                @Override
                                public void onResponse(String response) {

                                    JsonObject status=JsonParser.parseString(response).getAsJsonObject();
                                    if (status.get("status").getAsInt() == 1){

                                        SharedPreferences.Editor editor = sharedPref.edit();
                                        editor.putBoolean("IsLogged",true);
                                        editor.putString("Username",username.getText().toString());
                                        editor.commit();

                                        Intent loggin=new Intent(MainActivity.this, ListUserAlcoholMeasure.class);
                                        startActivity(loggin);
                                    }

                                }
                            }, new Response.ErrorListener() {
                        @Override
                        public void onErrorResponse(VolleyError error) {

                            if (error.networkResponse.statusCode == 400){
                                String body = null;
                                try {
                                    btnloggin.setEnabled(true);
                                    body = new String(error.networkResponse.data,"UTF-8");
                                    Integer status=JsonParser.parseString(body).getAsJsonObject().get("status").getAsInt();

                                    if (status == 0){
                                        Toast.makeText(MainActivity.this,"Usuario o clave incorrecta",Toast.LENGTH_SHORT).show();
                                    }

                                } catch (UnsupportedEncodingException e) {
                                    e.printStackTrace();
                                }
                            }

                        }

                    }){
                        @Override
                        protected Map<String,String> getParams(){
                            Map<String,String> params = new HashMap<String, String>();
                            params.put("Username",username.getText().toString());
                            params.put("Password",password.getText().toString());
                            return params;
                        }

                    };;
                    // Add the request to the RequestQueue.
                    requestQueue.add(strrequest);
                }
            });

        }


    }

    @Override
    public boolean onKeyDown(int keyCode, KeyEvent event) {

        if (keyCode == KeyEvent.KEYCODE_BACK){
            Intent intent = new Intent(Intent.ACTION_MAIN);
            intent.addCategory(Intent.CATEGORY_HOME);
            intent.setFlags(Intent.FLAG_ACTIVITY_NEW_TASK);
            startActivity(intent);
        }
        return super.onKeyDown(keyCode, event);
    }
}