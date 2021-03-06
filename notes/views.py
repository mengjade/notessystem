from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Notes
from django.urls import reverse_lazy, reverse
from django.shortcuts import get_object_or_404, render
from django.template import Context, loader
from django.http import HttpResponseRedirect,HttpResponse
from .forms import NotesForm

def IndexView(request):
    l = list(Notes.objects.values_list('note_type').distinct())
    object_list = [e[0] for e in l]
    context = {
        "object_list": object_list,
    }
    return render(request, 'notes/index.html', context)
        

def create_notes(request):
    form = NotesForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        notes = form.save(commit=False)
        notes.save()
        return render(request, 'notes/detail.html', {'notes': notes})
    context = {
        "form": form,
    }
    return render(request, 'notes/create_notes.html', context)

class modify_notes(UpdateView):
    model = Notes
    fields = ['note_type', 'sub_category', 'info_group','info_title', 'info_text', 'pic_file','comment']
    template_name_suffix = '_update_form'

def delete_notes(request, notes_id):
    n = Notes.objects.get(pk=notes_id)
    n.delete()
    temp = list(Notes.objects.values_list('note_type').distinct())
    object_list = []
    for e in temp:
        object_list.append(e[0])
    return render(request, 'notes/index.html', {'object_list': object_list})


def DetailView(request, pk):
    template= loader.get_template("notes/detail.html")
    notes = Notes.objects.get(pk=pk)
    context = {
        'notes': notes,
        'pk': pk,
    }
    return HttpResponse(template.render(context, request))

def NotesView(request,note_type):
    note_type_new=note_type[0].upper()+note_type[1:]

    all_data = Notes.objects.filter(note_type = note_type_new) 
    all_sub_cat_temp = list(Notes.objects.filter(note_type = note_type_new).values_list('sub_category').distinct())
    all_sub_cat = [e[0] for e in all_sub_cat_temp]

    all_group_temp = list(Notes.objects.filter(note_type = note_type_new).values_list('info_group').distinct())
    all_group = [e[0] for e in all_group_temp]

    show_sub_cats = 1

    template = loader.get_template('notes/notes_view.html')
    context = {
        'all_data': all_data,
        'all_sub_cat': all_sub_cat,
	    'note_type': note_type,
	    'all_group': all_group,
		'note_type_new': note_type_new,
		'show_sub_cats': show_sub_cats,
    }
    return HttpResponse(template.render(context, request))

def NotesSubView(request, note_type, sub_category):

	note_type_new=note_type[0].upper()+note_type[1:]

	all_data = Notes.objects.filter(note_type = note_type_new, sub_category = sub_category)
	all_sub_cat_temp = list(Notes.objects.filter(note_type = note_type_new).values_list('sub_category').distinct())
	all_sub_cat = [e[0] for e in all_sub_cat_temp]
    
	all_group_temp = list(Notes.objects.filter(note_type = note_type_new, sub_category = sub_category).values_list('info_group').distinct())
	all_group = [e[0] for e in all_group_temp]

	show_tc = 1	
	show_sub_cats = 1

	template = loader.get_template('notes/notes_view.html')
	context = {
        'all_data': all_data,
        'all_sub_cat': all_sub_cat,
        'sub_category': sub_category,
		'all_group': all_group,
		'note_type': note_type,
		'note_type_new': note_type_new,
		'show_tc': show_tc,
		'show_sub_cats': show_sub_cats,
	}
	return HttpResponse(template.render(context, request))
    
def NotesSubTC(request, note_type, sub_category):

	note_type_new=note_type[0].upper()+note_type[1:]

	all_data = Notes.objects.filter(note_type = note_type_new, sub_category = sub_category)
	all_sub_cat_temp = list(Notes.objects.filter(note_type = note_type_new).values_list('sub_category').distinct())
	all_sub_cat = [e[0] for e in all_sub_cat_temp]
    
	all_group_temp = list(Notes.objects.filter(note_type = note_type_new, sub_category = sub_category).values_list('info_group').distinct())
	all_group = [e[0] for e in all_group_temp]

	template = loader.get_template('notes/tc.html')
	print(sub_category)
	context = {
        'all_data': all_data,
        'sub_category': sub_category,
		'all_group': all_group,
		'note_type': note_type,
		'note_type_new': note_type_new,
	}
	return HttpResponse(template.render(context, request))


def NotesSubGroup(request, note_type, sub_category, info_group):

	note_type_new=note_type[0].upper()+note_type[1:]

	all_data = Notes.objects.filter(note_type = note_type_new, sub_category = sub_category, info_group = info_group)
	all_sub_cat_temp = list(Notes.objects.filter(note_type = note_type_new).values_list('sub_category').distinct())
	all_sub_cat = [e[0] for e in all_sub_cat_temp]
    
	all_group_temp = list(Notes.objects.filter(note_type = note_type_new, sub_category = sub_category, info_group = info_group).values_list('info_group').distinct())
	all_group = [e[0] for e in all_group_temp]

	show_labels = 1

	template = loader.get_template('notes/notes_view.html')
	context = {
        'all_data': all_data,
        'all_sub_cat': all_sub_cat,
        'sub_category': sub_category,
		'all_group': all_group,
		'note_type': note_type,
		'note_type_new': note_type_new,
        'show_labels': show_labels,
	}
	return HttpResponse(template.render(context, request))
