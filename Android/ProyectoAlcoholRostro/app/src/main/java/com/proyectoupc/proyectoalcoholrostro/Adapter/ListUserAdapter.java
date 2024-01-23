package com.proyectoupc.proyectoalcoholrostro.Adapter;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import com.proyectoupc.proyectoalcoholrostro.R;
import com.proyectoupc.proyectoalcoholrostro.UserMeasure.User;
import com.squareup.picasso.Picasso;

import java.util.List;

public class ListUserAdapter extends RecyclerView.Adapter<ListUserAdapter.ViewHolder>{
    private List<User> mData;
    private LayoutInflater inflater;
    private Context context;
    final ListUserAdapter.OnItemClickListener listener;
    public interface OnItemClickListener{
        void OnItemClick(User item);

    }
    public ListUserAdapter(List<User> mData, Context context, ListUserAdapter.OnItemClickListener listener){
        this.mData = mData;
        this.inflater = LayoutInflater.from(context);
        this.context = context;
        this.listener = listener;
    }
    @Override
    public int getItemCount(){ return mData.size(); }

    @NonNull
    @Override
    public ListUserAdapter.ViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View view = inflater.inflate(R.layout.view_rv_users, null);
        return new ListUserAdapter.ViewHolder(view);

    }

    @Override
    public void onBindViewHolder(@NonNull ListUserAdapter.ViewHolder holder, int position) {
        holder.bindData(mData.get(position));
    }

    public class ViewHolder extends RecyclerView.ViewHolder {
        ImageView iconimage;
        TextView fullname,DNI , Email, PhoneNumber;
        ViewHolder(View itemview){
            super(itemview);
            fullname = itemview.findViewById(R.id.NameUserData);
            DNI = itemview.findViewById(R.id.DNIUser);
            Email = itemview.findViewById(R.id.email);
            PhoneNumber = itemview.findViewById(R.id.PhoneNumber);
            iconimage =(ImageView) itemview.findViewById(R.id.imgperson);


        }
        void bindData(final User itemmed){
            fullname.setText(itemmed.getName()+" "+itemmed.getLastname());
            DNI.setText(itemmed.getDni());
            Email.setText(itemmed.getEmail());
            PhoneNumber.setText(itemmed.getPhoneNumber());
            //iconimage.set(itemmed.getFoto());
            Picasso.get().load("https://"+itemmed.getPicture()).into(iconimage);
            itemView.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View v) {
                    listener.OnItemClick(itemmed);
                }
            });
        }

    }
}
