package com.proyectoupc.proyectoalcoholrostro.JavaActivities.User;

import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.util.Log;
import android.view.KeyEvent;
import android.view.Menu;
import android.view.MenuInflater;
import android.view.MenuItem;

import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;
import androidx.swiperefreshlayout.widget.SwipeRefreshLayout;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;
import com.google.gson.JsonArray;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import com.google.gson.JsonParser;
import com.proyectoupc.proyectoalcoholrostro.Adapter.RecycleViewAdapter;
import com.proyectoupc.proyectoalcoholrostro.Constants;
import com.proyectoupc.proyectoalcoholrostro.MainActivity;
import com.proyectoupc.proyectoalcoholrostro.R;
import com.proyectoupc.proyectoalcoholrostro.RView.EndlessRecyclerViewScrollListener;
import com.proyectoupc.proyectoalcoholrostro.UserMeasure.User;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class ListUserAlcoholMeasure extends AppCompatActivity {

    private EndlessRecyclerViewScrollListener scrollListener;
    private RecyclerView rview;
    public static User user;
    public List<User> arrayUser= new ArrayList<>();
    RecycleViewAdapter ladapter;
    SharedPreferences sharedPref;
    SwipeRefreshLayout swipeRefreshLayout;
    LinearLayoutManager lmanager;
    private boolean resetendlessrv = false;

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_list_user_alcohol_measure);

        //get shared preferences
        sharedPref = getSharedPreferences("LogginData", Context.MODE_PRIVATE);

    }

    @Override
    protected void onStart() {
        super.onStart();
        if (sharedPref.getBoolean("IsLogged",false)){

            rview = (RecyclerView) findViewById(R.id.recicleviewalc);
            swipeRefreshLayout = (SwipeRefreshLayout) findViewById(R.id.swipeRefreshLayout);

            lmanager = new LinearLayoutManager(this);
            rview.setLayoutManager(lmanager);


            loadfirstDataFromApi();

            scrollListener = new EndlessRecyclerViewScrollListener(lmanager) {
                @Override
                public void onLoadMore(int page, int totalItemsCount, RecyclerView view) {
                    // Triggered only when new data needs to be appended to the list
                    // Add whatever code is needed to append new items to the bottom of the list
                    //if (resetendlessrv) {resetState();resetendlessrv=false;}
                    loadNextDataFromApi(page+1);
                }

            };
            // Adds the scroll listener to RecyclerView

            rview.addOnScrollListener(scrollListener);
        }
        else {
            Intent exit = new Intent(getApplicationContext(), MainActivity.class);
            startActivity(exit);
        }
    }

    public void loadfirstDataFromApi(){

        Log.d("loadfirstDataFromApi Page",Integer.toString(1));
        RequestQueue queue = Volley.newRequestQueue(getApplicationContext());

        // Request a string response from the provided URL.
        StringRequest stringRequest = new StringRequest(Request.Method.POST, Constants.url_api +"/proy_control_alc/user/datauseralcohol.php",
                new Response.Listener<String>() {
                    @Override
                    public void onResponse(String response) {
                        // Display the first 500 characters of the response string.
                        try {
                            Log.d("response :",response);
                            JsonObject objresponse= JsonParser.parseString(response).getAsJsonObject();
                            JsonObject objmodel = objresponse.get("objModel").getAsJsonObject();

                            JsonArray medalcohol = objmodel.getAsJsonArray("elements");
                            arrayUser.clear();
                            for (JsonElement obj : medalcohol) {

                                JsonObject jsonobjalc = obj.getAsJsonObject();
                                int     id     = jsonobjalc.get("id").getAsInt();
                                double     Alc_mgL     = jsonobjalc.get("Alc_mgL").getAsDouble();
                                double     Alc_BAC     = jsonobjalc.get("Alc_BAC").getAsDouble();
                                int     Ing_Alcohol = jsonobjalc.get("Ing_Alcohol").getAsInt();
                                String     Picture     = jsonobjalc.get("Picture").getAsString();
                                String     Date     = jsonobjalc.get("Date").getAsString();
                                JsonObject Userobj = jsonobjalc.get("User").getAsJsonObject();
                                String     DNI     = Userobj.get("DNI").getAsString();
                                String  Name = Userobj.get("Name").getAsString();
                                String  Lastname = Userobj.get("Lastname").getAsString();

                                user = new User(DNI);
                                user.setName(Name);
                                user.setLastname(Lastname);
                                user.addalcoholmeasure(id, Alc_mgL, Alc_BAC, Ing_Alcohol, Picture, Date);
                                arrayUser.add(user);

                            }

                            ladapter = new RecycleViewAdapter(arrayUser, getApplicationContext(), new RecycleViewAdapter.OnItemClickListener() {
                                @Override
                                public void OnItemClick(User item) {
                                    movetoother(item);
                                }
                            });
                            rview.setAdapter(ladapter);
                            // SetOnRefreshListener on SwipeRefreshLayout
                            swipeRefreshLayout.setOnRefreshListener(new SwipeRefreshLayout.OnRefreshListener() {
                                @Override
                                public void onRefresh() {
                                    swipeRefreshLayout.setRefreshing(false);
                                    RearrangeItems();
                                }
                            });

                        }
                        catch (Exception exc){

                        }

                    }
                }, new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {
                //textView.setText("That didn't work!");
            }
        }){
            @Override
            protected Map<String,String> getParams(){
                Map<String,String> params = new HashMap<String, String>();

                params.put("username",sharedPref.getString("Username","admin"));
                params.put("sizelist",Integer.toString(7));
                params.put("numberpage",Integer.toString(1));
                params.put("startdate","2021-06-30 00:00:00");
                params.put("enddate","2025-10-30 23:00:00");
                return params;
            }

        };
        // Add the request to the RequestQueue.
        queue.add(stringRequest);
    }
    public void movetoother(User med){

    }
    public void loadNextDataFromApi(int offset) {
        // Send an API request to retrieve appropriate paginated data
        //  --> Send the request including an offset value (i.e `page`) as a query parameter.
        //  --> Deserialize and construct new model objects from the API response
        //  --> Append the new data objects to the existing set of items inside the array of items
        //  --> Notify the adapter of the new items made with `notifyItemRangeInserted()`
        Log.d("loadNextDataFromApi Page",Integer.toString(offset));
        RequestQueue queue = Volley.newRequestQueue(getApplicationContext());


        // Request a string response from the provided URL.
        StringRequest stringRequest = new StringRequest(Request.Method.POST, Constants.url_api +"/proy_control_alc/user/datauseralcohol.php",
                new Response.Listener<String>() {
                    @Override
                    public void onResponse(String response) {
                        // Display the first 500 characters of the response string.
                        try {
                            JsonObject objresponse= JsonParser.parseString(response).getAsJsonObject();
                            JsonObject objmodel = objresponse.get("objModel").getAsJsonObject();

                            JsonArray medalcohol = objmodel.getAsJsonArray("elements");

                            for (JsonElement obj : medalcohol) {

                                JsonObject jsonobjalc = obj.getAsJsonObject();
                                int     id     = jsonobjalc.get("id").getAsInt();
                                double     Alc_mgL     = jsonobjalc.get("Alc_mgL").getAsDouble();
                                double     Alc_BAC     = jsonobjalc.get("Alc_BAC").getAsDouble();
                                int      Ing_Alcohol = jsonobjalc.get("Ing_Alcohol").getAsInt();
                                String     Picture     = jsonobjalc.get("Picture").getAsString();
                                String     Date     = jsonobjalc.get("Date").getAsString();
                                JsonObject Userobj = jsonobjalc.get("User").getAsJsonObject();
                                String     DNI     = Userobj.get("DNI").getAsString();
                                String  Name = Userobj.get("Name").getAsString();
                                String  Lastname = Userobj.get("Lastname").getAsString();

                                user = new User(DNI);
                                user.setName(Name);
                                user.setLastname(Lastname);
                                user.addalcoholmeasure(id, Alc_mgL, Alc_BAC, Ing_Alcohol, Picture, Date);
                                arrayUser.add(user);

                            }
                            //arrayUser.clear();
                            ladapter.notifyDataSetChanged();

                        }
                        catch (Exception exc){

                        }



                    }
                }, new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {
                //textView.setText("That didn't work!");
            }
        }){
            @Override
            protected Map<String,String> getParams(){
                Map<String,String> params = new HashMap<String, String>();

                params.put("username",sharedPref.getString("Username","admin"));
                params.put("sizelist",Integer.toString(7));
                params.put("numberpage",Integer.toString(offset));
                params.put("startdate","2022-06-30 00:00:00");
                params.put("enddate","2024-10-30 23:00:00");
                return params;
            }

        };
        // Add the request to the RequestQueue.
        queue.add(stringRequest);
    }
    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        MenuInflater inflater = getMenuInflater();
        inflater.inflate(R.menu.items, menu);
        return true;
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

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle item selection
        switch (item.getItemId()) {
            case R.id.idcerrarsesión:
                SharedPreferences.Editor spclosesession = sharedPref.edit();
                spclosesession.clear();
                spclosesession.apply();
                startActivity(new Intent(getApplicationContext(),this.getClass()));
                return true;
            default:
                return super.onOptionsItemSelected(item);
        }
    }
    private void RearrangeItems(){
        loadfirstDataFromApi();

        scrollListener = new EndlessRecyclerViewScrollListener(lmanager) {
            @Override
            public void onLoadMore(int page, int totalItemsCount, RecyclerView view) {
                // Triggered only when new data needs to be appended to the list
                // Add whatever code is needed to append new items to the bottom of the list
                loadNextDataFromApi(page+1);
            }

        };
        // Adds the scroll listener to RecyclerView
        rview.clearOnScrollListeners();
        rview.addOnScrollListener(scrollListener);
    }
}
