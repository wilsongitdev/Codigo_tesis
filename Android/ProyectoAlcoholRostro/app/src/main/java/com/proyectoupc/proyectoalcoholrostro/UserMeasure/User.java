package com.proyectoupc.proyectoalcoholrostro.UserMeasure;

import java.text.SimpleDateFormat;
import java.time.LocalDateTime;
import java.time.ZoneId;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;
import java.util.Date;

public class User {
    private String email;
    private String name;
    private String lastname;
    private String dni;
    private String phoneNumber;
    private String address;
    private String city;
    private String district;
    private String country;
    private String occupation;
    private String dateRegister;
    private String picture;



    private ArrayList<Measure> alcoholmeasure = new ArrayList<>();

    public  User(String dni){
        this.dni = dni;
    }

    public void addalcoholmeasure(int id, double alcoholMgl, double alcoholBAC, boolean Ing_Alcohol, String urlPicture, String date){
        alcoholmeasure.add(new User.Measure(id, alcoholMgl, alcoholBAC, Ing_Alcohol, urlPicture, date));
    }

    public ArrayList<Measure> getAlcoholmeasure() {
        return alcoholmeasure;
    }

    public void resetAlcoholmeasure(){
        alcoholmeasure.clear();
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getLastname() {
        return lastname;
    }

    public void setLastname(String lastname) {
        this.lastname = lastname;
    }

    public String getDni() {
        return dni;
    }

    public void setDni(String dni) {
        this.dni = dni;
    }

    public String getPhoneNumber() {
        return phoneNumber;
    }

    public void setPhoneNumber(String phoneNumber) {
        this.phoneNumber = phoneNumber;
    }

    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }

    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
    }

    public String getDistrict() {
        return district;
    }

    public void setDistrict(String district) {
        this.district = district;
    }

    public String getCountry() {
        return country;
    }

    public void setCountry(String country) {
        this.country = country;
    }

    public String getOccupation() {
        return occupation;
    }

    public void setOccupation(String occupation) {
        this.occupation = occupation;
    }

    public String getDateRegister() {
        return dateRegister;
    }

    public void setDateRegister(String dateRegister) {
        this.dateRegister = dateRegister;
    }

    public String getPicture() {
        return picture;
    }

    public void setPicture(String picture) {
        this.picture = picture;
    }

    public static class Measure{
        private int id;
        private double alcoholMgl;
        private double alcoholBAC;
        private boolean Ing_Alcohol;
        private String urlPicture;
        private String date;


        public Measure(int id, double alcoholMgl, double alcoholBAC, boolean Ing_Alcohol, String urlPicture, String date) {
            this.id = id;
            this.alcoholMgl = alcoholMgl;
            this.alcoholBAC = alcoholBAC;
            this.Ing_Alcohol = Ing_Alcohol;
            this.urlPicture = urlPicture;
            this.date = date;
        }

        public int getId() {
            return id;
        }

        public double getAlcoholMgl() {
            return alcoholMgl;
        }

        public double getAlcoholBAC() {
            return alcoholBAC;
        }

        public String getUrlPicture() {
            return urlPicture;
        }

        public boolean getIng_Alcohol() {return Ing_Alcohol;}

        public String getDate() {
            LocalDateTime dateISO = LocalDateTime.parse(date, DateTimeFormatter.ISO_OFFSET_DATE_TIME);
            return dateISO.format(DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss"));
        }
    }
}
