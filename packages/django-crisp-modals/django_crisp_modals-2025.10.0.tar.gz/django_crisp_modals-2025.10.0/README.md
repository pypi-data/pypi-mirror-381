
django-crisp-modals
===================

django-crisp-modals is a Django app which provides support for ajax Django Crispy Forms
inside Bootstrap 5 modal dialogs.  The app provides various views, form classes, templates and 
javascript.  A demo site showcasing an example configuration various features, is available in the repository.


Quick start
-----------

1. Add "crisp_modals", and "crispy_forms" to your INSTALLED_APPS setting like this::
    ```python
    INSTALLED_APPS = [
        ...,
        "crispy_forms",
        "crispy_bootstrap5",
        "crisp_modals",
    ]
2. Add the following to your settings.py file::

    ```python
    CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
    CRISPY_TEMPLATE_PACK = "bootstrap5"

3. Include the `crisp_modals/modals.min.js` within your base template after jQuery
   and add a blank modal div to the bottom of the body tag.  The modal div should have the id: `modal-target`. 
   Then initialize the modal target.  For example:

    ```html  
    {% load static %}
    ...
    <div id="modal-target"></div>
    <script src="https://cdn.jsdelivr.net/npm/jquery@3.7.1/dist/jquery.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/jquery-form@4.3.0/dist/jquery.form.min.js"></script>
    <script src="{% static 'crisp_modals/modals.min.js' %}"></script>
    <script>
        $(document).ready(function() {
            $('#modal-target').initModal({
                setup: function (element) {
                    // This function is called for each modal that is opened.
                    // You can add any additional setup code here.
                    ...
                }
            });
        });
    </script>
   
4. Create forms as follows. The main crispy-forms helper is available as `self.body` within the forms. 
   A footer helper is also available as `self.footer`, with 'submit' and 'reset' buttons already included. To override
   the footer buttons, you can use the `self.footer.clear()` method to remove the default buttons and then add your own.
   
   ```python
   from crisp_modals.forms import ModalModelForm, Row, FullWidth

    class PollForm(ModalModelForm):
         class Meta:
              model = Poll
              fields = ['question', 'pub_date']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.body.append(
            Row(
                FullWidth('question', placeholder='Enter your question'),
            ),
            Row(
                FullWidth('pub_date', placeholder='Enter the publication date'),
            )
        )

5. In your views, use the ModalCreateView, ModalUpdateView, ModalConfirmView, and ModalDeleteView classes as follows. Include
   `delete_url` in the form kwargs for the ModalUpdateView class to show the delete button within the form. By default,
    the form will be submitted to the same URL as the view, but you can override this by adding a `form_action` variable 
    to the form keyword arguments.
    
    ```python
    from crisp_modals.views import ModalCreateView, ModalUpdateView, ModalDeleteView

    class PollCreateView(ModalCreateView):
        model = Poll
        form_class = PollForm

   
    class PollEditView(ModalUpdateView):
        model = Poll
        form_class = PollForm
        
   
        def get_form_kwargs(self):
            kwargs = super().get_form_kwargs()
            # If you want the form submitted to a different url, override the `form_action` variable.
            kwargs['form_action'] = ...  # e.g., reverse('polls:poll-update', kwargs={'pk': self.object.pk})
            return kwargs
   
        def get_delete_url(self):
            # If you want to show a delete button in the form, you can return the URL for the delete confirmation view.
            return reverse('polls:poll-delete', kwargs={'pk': self.object.pk})
 
   
    class PollConfirView(ModalConfirmView):
        model = Poll
        
        def get_context_data(self):
            context = super().get_context_data()
            context['title'] = 'Close Poll'
            context['message'] = 'Are you sure you want to close this poll?'
            return context
   
        def confirmed(self, *args, **kwargs):
            # Logic to close the poll
            self.object.close()  # Assuming the Poll model has a close method
            return super().confirmed()
      
   
    class PollDeleteView(ModalDeleteView):
        model = Poll
   

    
6. To distinguish regular links from links that target modals, use the 'data-modal-url' attribute instead of href.
   For example:

    ```html
    <a href="#0" data-modal-url="{% url 'polls:poll-create' %}" class="modal-link">Create Poll</a>
    <a href="#0" data-modal-url="{% url 'polls:poll-update' pk=poll.pk %}">Update Poll</a>

> Note: 
> 
> The `data-modal-url` attribute should contain the url of the view that will render the modal. It doesn't have to 
> return a form. Non-form modal content can be rendered by overriding the `modal_content` block in the modal template
> `crisp_modals/modal.html`.  The following blocks are available for overriding: `modal_header`, `modal_body`, `modal_footer`,
> `modal_scripts`.  The `modal_scripts` block should be used to include any additional JavaScript required for the modal 
> content per-instance. Any code needed for all modals should go in the `initModal` setup option.